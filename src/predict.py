import pandas as pd
import joblib

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("models/aqi_xgboost.pkl")

# ==========================================
# LOAD FINAL DATASET
# ==========================================

df = pd.read_csv("data/final_dataset.csv")

# ==========================================
# SELECT CITY
# ==========================================

city = input("Enter City: ")

city_df = df[df["City"] == city]

if city_df.empty:
    print("City not found!")
    exit()

# ==========================================
# TAKE LATEST RECORD
# ==========================================

latest = city_df.iloc[-1:]

# ==========================================
# REMOVE TARGET
# ==========================================

X = latest.drop(columns=[
    "AQI",
    "Date",
    "AQI_Bucket"
], errors="ignore")

# ==========================================
# ONE-HOT ENCODING
# ==========================================

X = pd.get_dummies(X)

# ==========================================
# MATCH TRAINING FEATURES
# ==========================================

model_features = model.get_booster().feature_names

for col in model_features:
    if col not in X.columns:
        X[col] = 0

X = X[model_features]

# ==========================================
# PREDICT
# ==========================================

prediction = model.predict(X)[0]

# ==========================================
# RESULTS
# ==========================================

print("\n" + "="*50)
print("AI AIR QUALITY PREDICTION")
print("="*50)

print(f"City           : {city}")
print(f"Actual AQI     : {latest['AQI'].values[0]:.2f}")
print(f"Predicted AQI  : {prediction:.2f}")

difference = abs(prediction - latest["AQI"].values[0])

print(f"Difference     : {difference:.2f}")

# ==========================================
# AQI CATEGORY
# ==========================================

if prediction <= 50:
    status = "Good 🟢"
elif prediction <= 100:
    status = "Moderate 🟡"
elif prediction <= 200:
    status = "Poor 🟠"
elif prediction <= 300:
    status = "Very Poor 🔴"
else:
    status = "Severe ⚫"

print(f"Category       : {status}")

print("="*50)
