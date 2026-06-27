import pandas as pd

print("=" * 60)
print("Loading Dataset...")
print("=" * 60)

# ------------------------------------------------
# LOAD CSV
# ------------------------------------------------

df = pd.read_csv("data/india_aqi_weather_2015_2024.csv")

print("Original Shape :", df.shape)

# ------------------------------------------------
# REMOVE DUPLICATES
# ------------------------------------------------

df = df.drop_duplicates()

# ------------------------------------------------
# CONVERT DATE
# ------------------------------------------------

df["Date"] = pd.to_datetime(df["Date"])

# ------------------------------------------------
# SORT DATA
# ------------------------------------------------

df = df.sort_values(["City", "Date"])

# ------------------------------------------------
# FILL MISSING VALUES
# ------------------------------------------------

numeric_columns = df.select_dtypes(include=["number"]).columns

for col in numeric_columns:
    df[col] = df.groupby("City")[col].transform(
        lambda x: x.interpolate()
    )

df = df.fillna(method="bfill")
df = df.fillna(method="ffill")

# ------------------------------------------------
# REMOVE REMAINING EMPTY ROWS
# ------------------------------------------------

df = df.dropna()

print("After Cleaning :", df.shape)

# ------------------------------------------------
# SAVE
# ------------------------------------------------

df.to_csv("data/cleaned_dataset.csv", index=False)

print("\nDataset Saved Successfully!")

print("\nSaved as:")
print("data/cleaned_dataset.csv")

print("\nColumns:")

print(df.columns.tolist())

print("\nFirst Five Rows:\n")

print(df.head())
