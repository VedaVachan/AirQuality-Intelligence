import pandas as pd

print("=" * 60)
print("Loading Cleaned Dataset...")
print("=" * 60)

df = pd.read_csv("data/cleaned_dataset.csv")

df["Date"] = pd.to_datetime(df["Date"])

# ------------------------------------
# SORT
# ------------------------------------

df = df.sort_values(["City", "Date"])

# ------------------------------------
# TIME FEATURES
# ------------------------------------

df["year"] = df["Date"].dt.year
df["month"] = df["Date"].dt.month
df["day"] = df["Date"].dt.day
df["day_of_week"] = df["Date"].dt.dayofweek
df["day_of_year"] = df["Date"].dt.dayofyear
df["week_of_year"] = df["Date"].dt.isocalendar().week.astype(int)

# ------------------------------------
# AQI HISTORY
# ------------------------------------

df["aqi_lag1"] = df.groupby("City")["AQI"].shift(1)
df["aqi_lag3"] = df.groupby("City")["AQI"].shift(3)
df["aqi_lag7"] = df.groupby("City")["AQI"].shift(7)

# ------------------------------------
# ROLLING FEATURES
# ------------------------------------

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

# ------------------------------------
# REMOVE EMPTY ROWS
# ------------------------------------

df.dropna(inplace=True)

# ------------------------------------
# SAVE
# ------------------------------------

df.to_csv("data/final_dataset.csv", index=False)

print("\nFeature Engineering Completed!")

print("\nFinal Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())
