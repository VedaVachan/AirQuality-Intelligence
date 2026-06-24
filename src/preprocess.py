import pandas as pd

aqi = pd.read_csv("data/aqi_hyderabad.csv")
weather = pd.read_csv("data/weather_hyderabad.csv")

aqi["date"] = pd.to_datetime(aqi["date"])
weather["date"] = pd.to_datetime(weather["date"])

aqi = aqi[["date", "Index Value"]]
aqi.rename(columns={"Index Value": "aqi"}, inplace=True)

merged = pd.merge(aqi, weather, on="date", how="inner")

merged.to_csv("data/merged_data.csv", index=False)

print("Merged Shape:", merged.shape)
print(merged.head())