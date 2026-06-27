import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from xgboost import XGBRegressor

# =====================================
# LOAD DATA
# =====================================

df = pd.read_csv("data/final_dataset.csv")

print("=" * 60)
print("Dataset Loaded")
print("=" * 60)
print(df.head())

# =====================================
# DROP UNUSED COLUMNS
# =====================================

drop_columns = [
    "Date",
    "AQI_Bucket"
]

for col in drop_columns:
    if col in df.columns:
        df.drop(columns=col, inplace=True)

# =====================================
# ENCODE CITY
# =====================================

df = pd.get_dummies(
    df,
    columns=["City"],
    drop_first=True
)

# =====================================
# FEATURES & TARGET
# =====================================

X = df.drop(columns=["AQI"])

y = df["AQI"]

print("\nNumber of Features :", X.shape[1])

# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples  :", len(X_test))

# =====================================
# MODEL
# =====================================

model = XGBRegressor(
    n_estimators=400,
    learning_rate=0.05,
    max_depth=8,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="reg:squarederror",
    random_state=42
)

# =====================================
# TRAIN
# =====================================

print("\nTraining Model...\n")

model.fit(X_train, y_train)

print("Training Completed!")

# =====================================
# PREDICT
# =====================================

predictions = model.predict(X_test)

# =====================================
# EVALUATION
# =====================================

mae = mean_absolute_error(y_test, predictions)

rmse = mean_squared_error(
    y_test,
    predictions,
    squared=False
)

r2 = r2_score(
    y_test,
    predictions
)

print("\n")
print("=" * 60)
print("MODEL PERFORMANCE")
print("=" * 60)

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# =====================================
# FEATURE IMPORTANCE
# =====================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 20 Important Features\n")

print(importance.head(20))

# =====================================
# SAVE MODEL
# =====================================

joblib.dump(
    model,
    "models/aqi_xgboost.pkl"
)

print("\n")
print("=" * 60)
print("Model Saved Successfully")
print("Location : models/aqi_xgboost.pkl")
print("=" * 60)
