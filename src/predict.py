import pandas as pd
import joblib

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("models/aqi_xgboost.pkl")

model_features = joblib.load(
    "models/model_features.pkl"
)


# ==========================================
# AQI CATEGORY
# ==========================================

def get_category(aqi):

    if aqi <= 50:
        return "🟢 Good"

    elif aqi <= 100:
        return "🟡 Moderate"

    elif aqi <= 200:
        return "🟠 Poor"

    elif aqi <= 300:
        return "🔴 Very Poor"

    return "⚫ Severe"


# ==========================================
# PREDICT FUNCTION
# ==========================================

def predict_aqi(latest_row, model, model_features):

    X = latest_row.drop(
        columns=[
            "AQI",
            "Date",
            "AQI_Bucket"
        ],
        errors="ignore"
    )

    X = pd.get_dummies(
        X,
        columns=["City"]
    )

    for col in model_features:

        if col not in X.columns:
            X[col] = 0

    X = X[model_features]

    prediction = model.predict(X)[0]

    return float(prediction)


# ==========================================
# COMMAND LINE MODE
# ==========================================

if __name__ == "__main__":

    print("=" * 60)
    print("AI AIR QUALITY PREDICTION")
    print("=" * 60)

    df = pd.read_csv("data/final_dataset.csv")

    cities = sorted(df["City"].unique())

    print("\nAvailable Cities:\n")

    for city in cities:
        print("-", city)

    selected_city = input("\nEnter City Name: ").strip()

    if selected_city not in cities:
        print("\nCity not found!")
        exit()

    city_df = df[df["City"] == selected_city]

    latest = city_df.iloc[-1:].copy()

    actual_aqi = latest["AQI"].values[0]

    prediction = predict_aqi(
        latest,
        model,
        model_features
    )

    print("\n" + "=" * 60)

    print(f"City            : {selected_city}")
    print(f"Actual AQI      : {actual_aqi:.2f}")
    print(f"Predicted AQI   : {prediction:.2f}")
    print(f"Difference      : {abs(actual_aqi-prediction):.2f}")
    print(f"Category        : {get_category(prediction)}")

    print("=" * 60)