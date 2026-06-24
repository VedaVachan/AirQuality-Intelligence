import os
import joblib
import numpy as np
import pandas as pd

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

print("Loading dataset...")

# Load dataset
df = pd.read_csv("data/final_dataset.csv")

print("Dataset Shape:", df.shape)

# Features
X = df[
    [
        "temperature",
        "rainfall",
        "wind_speed",
        "month",
        "day_of_year",
        "aqi_lag1",
        "aqi_7day_avg"
    ]
]

# Target
y = df["aqi"]

print("Feature Shape:", X.shape)

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples :", len(X_test))

# XGBoost Model
model = XGBRegressor(
    n_estimators=300,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    objective="reg:squarederror"
)

print("\nTraining Model...")

# Train
model.fit(X_train, y_train)

print("Training Completed!")

# Predictions
preds = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, preds)
rmse = np.sqrt(mean_squared_error(y_test, preds))
r2 = r2_score(y_test, preds)

print("\n========== MODEL RESULTS ==========")
print("MAE :", round(mae, 2))
print("RMSE:", round(rmse, 2))
print("R2  :", round(r2, 4))
print("===================================")

# Create models folder automatically
os.makedirs("models", exist_ok=True)

# Save model
model_path = "models/aqi_xgboost.pkl"

joblib.dump(model, model_path)

print("\nModel Saved Successfully!")
print("Location:", model_path)
