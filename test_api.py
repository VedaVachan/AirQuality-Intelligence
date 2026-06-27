from src.air_api import *

city = "Hyderabad"

weather = get_live_weather(city)
air = get_live_air_quality(city)

print("\nWEATHER")
print(weather)

print("\nAIR QUALITY")
print(air)

print("\nAQI STATUS")
print(get_aqi_status(air["aqi"]))

print("\nAQI SCORE")
print(convert_aqi_to_score(air["aqi"]))