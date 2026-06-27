import pandas as pd

# ======================================================
# FEATURE ENGINEERING FOR AIR QUALITY DATASET
# ======================================================

print("=" * 60)
print("Loading Cleaned Dataset...")
print("=" * 60)

# ------------------------------------------------------
# LOAD DATASET
# ------------------------------------------------------

df = pd.read_csv("data/cleaned_dataset.csv")

# ------------------------------------------------------
# CONVERT DATE
# ------------------------------------------------------

df["Date"] = pd.to_datetime(df["Date"])

# ------------------------------------------------------
# SORT DATA
# ------------------------------------------------------

df = df.sort_values(["City", "Date"])
df = df.reset_index(drop=True)

# ======================================================
# TIME FEATURES
# ======================================================

print("Creating Time Features...")

df["year"] = df["Date"].dt.year
df["month"] = df["Date"].dt.month
df["day"] = df["Date"].dt.day
df["day_of_week"] = df["Date"].dt.dayofweek
df["day_of_year"] = df["Date"].dt.dayofyear
df["week_of_year"] = df["Date"].dt.isocalendar().week.astype(int)

# ======================================================
# AQI LAG FEATURES
# ======================================================

print("Creating Lag Features...")

df["aqi_lag1"] = df.groupby("City")["AQI"].shift(1)
df["aqi_lag3"] = df.groupby("City")["AQI"].shift(3)
df["aqi_lag7"] = df.groupby("City")["AQI"].shift(7)

# ======================================================
# ROLLING FEATURES
# ======================================================

print("Creating Rolling Statistics...")

df["aqi_3day_avg"] = (
    df.groupby("City")["AQI"]
      .transform(lambda x: x.rolling(3).mean())
)

df["aqi_7day_avg"] = (
    df.groupby("City")["AQI"]
      .transform(lambda x: x.rolling(7).mean())
)

df["aqi_7day_max"] = (
    df.groupby("City")["AQI"]
      .transform(lambda x: x.rolling(7).max())
)

df["aqi_7day_min"] = (
    df.groupby("City")["AQI"]
      .transform(lambda x: x.rolling(7).min())
)

df["aqi_7day_std"] = (
    df.groupby("City")["AQI"]
      .transform(lambda x: x.rolling(7).std())
)

# ======================================================
# DROP ROWS CREATED BY SHIFT/ROLLING
# ======================================================

print("Removing Empty Rows...")

df.dropna(inplace=True)

df.reset_index(drop=True, inplace=True)

# ======================================================
# SAVE DATASET
# ======================================================

df.to_csv(
    "data/final_dataset.csv",
    index=False
)

# ======================================================
# SUMMARY
# ======================================================

print("\n" + "=" * 60)
print("FEATURE ENGINEERING COMPLETED SUCCESSFULLY")
print("=" * 60)

print(f"\nFinal Dataset Shape : {df.shape}")

print(f"\nTotal Features : {len(df.columns)}")

print(f"\nTotal Cities : {df['City'].nunique()}")

print("\nCities Included:\n")

for city in sorted(df["City"].unique()):
    print("✓", city)

print("\nColumns:\n")

for col in df.columns:
    print(col)

print("\nFirst 5 Rows:\n")

print(df.head())

print("\nDataset saved successfully!")

print("Location : data/final_dataset.csv")

print("=" * 60)
