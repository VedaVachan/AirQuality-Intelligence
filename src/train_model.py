import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from xgboost import XGBRegressor

print("="*60)
print("Loading Final Dataset...")
print("="*60)

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv("data/final_dataset.csv")

print("\nDataset Shape:", df.shape)

# ==========================================
# DROP UNUSED COLUMNS
# ==========================================

X = df.drop(columns=[
    "AQI",
    "Date",
    "AQI_Bucket"
])

y = df["AQI"]

# ==========================================
# ONE HOT ENCODE CITY
# ==========================================

X = pd.get_dummies(
    X,
    columns=["City"],
    drop_first=True
)

print("\nFeature Matrix:", X.shape)

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# ==========================================
# MODEL
# ==========================================

model = XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=8,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="reg:squarederror",
    random_state=42
)

print("\nTraining Model...\n")

model.fit(X_train, y_train)

print("Training Completed!")

# ==========================================
# PREDICTION
# ==========================================

pred = model.predict(X_test)

# ==========================================
# METRICS
# ==========================================

mae = mean_absolute_error(y_test, pred)

rmse = mean_squared_error(
    y_test,
    pred
) ** 0.5

r2 = r2_score(
    y_test,
    pred
)

print("\n")
print("="*60)
print("MODEL PERFORMANCE")
print("="*60)

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# ==========================================
# FEATURE IMPORTANCE
# ==========================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 20 Features\n")

print(importance.head(20))

# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(model, "models/aqi_xgboost.pkl")

joblib.dump(
    X.columns.tolist(),
    "models/model_features.pkl"
)

print("\n")
print("="*60)
print("MODEL SAVED SUCCESSFULLY")
print("="*60)

print("Saved:")
print("models/aqi_xgboost.pkl")
print("models/model_features.pkl")