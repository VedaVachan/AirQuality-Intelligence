import joblib
import pandas as pd

# Load model
model = joblib.load("models/aqi_xgboost.pkl")

# Example input
sample = pd.DataFrame([{
    "temperature": 32,
    "rainfall": 0,
    "wind_speed": 12,
    "month": 6,
    "day_of_year": 175,
    "aqi_lag1": 120,
    "aqi_7day_avg": 115
}])

prediction = model.predict(sample)

print("Predicted AQI:", round(prediction[0], 2))
