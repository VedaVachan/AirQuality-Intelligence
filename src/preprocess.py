import pandas as pd

# ==========================================
# Load Dataset
# ==========================================

df = pd.read_excel("data/india_aqi_weather_2015_2024.csv")

print("Original Shape:", df.shape)

# ==========================================
# Rename Columns
# ==========================================

df.rename(columns={
    "PM2.5": "PM25"
}, inplace=True)

# ==========================================
# Convert Date
# ==========================================

df["Date"] = pd.to_datetime(df["Date"])

# ==========================================
# Remove Duplicate Rows
# ==========================================

df.drop_duplicates(inplace=True)

# ==========================================
# Sort Data
# ==========================================

df.sort_values(
    by=["City", "Date"],
    inplace=True
)

# ==========================================
# Fill Missing Values
# ==========================================

numeric_columns = df.select_dtypes(include="number").columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# ==========================================
# Save Clean Dataset
# ==========================================

df.to_csv(
    "data/cleaned_dataset.csv",
    index=False
)

print("\nCleaning Completed Successfully!")

print("\nFinal Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())
