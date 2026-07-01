"""
============================================================
HELPER FUNCTIONS
AI Powered Urban Air Quality Intelligence
============================================================
"""

from utils.constants import AQI_SCALE

from src.predict import predict_aqi


# ============================================================
# CONVERT OPENWEATHER AQI -> CPCB AQI
# ============================================================

def convert_api_aqi(api_aqi):
    """
    Convert OpenWeather AQI (1-5)
    into approximate CPCB AQI.
    """

    return AQI_SCALE.get(
        int(api_aqi),
        0
    )


# ============================================================
# FILTER DATA FOR SELECTED CITY
# ============================================================

def get_city_history(df, city):
    """
    Return historical dataframe
    for selected city.
    """

    city_df = df[
        df["City"] == city
    ].copy()

    city_df.sort_values(
        "Date",
        inplace=True
    )

    city_df.reset_index(
        drop=True,
        inplace=True
    )

    return city_df


# ============================================================
# AQI PREDICTION
# ============================================================

def get_prediction(city_df, model, model_features):
    """
    Predict AQI using trained
    XGBoost model.
    """

    latest = city_df.iloc[-1:].copy()

    prediction = predict_aqi(
        latest,
        model,
        model_features
    )

    return float(prediction)


# ============================================================
# VISIBILITY STATUS
# ============================================================

def get_visibility(current_aqi):
    """
    Visibility level based on AQI.
    """

    if current_aqi <= 100:
        return "Good"

    elif current_aqi <= 150:
        return "Moderate"

    else:
        return "Poor"


# ============================================================
# HEALTH SCORE
# ============================================================

def calculate_health_score(current_aqi):
    """
    Calculate environmental
    health score.
    """

    score = max(
        0,
        100 - int(current_aqi / 5)
    )

    return score


# ============================================================
# AQI STATUS
# ============================================================

def get_aqi_level(current_aqi):
    """
    AQI category.
    """

    if current_aqi <= 50:
        return "Good"

    elif current_aqi <= 100:
        return "Moderate"

    elif current_aqi <= 200:
        return "Poor"

    elif current_aqi <= 300:
        return "Very Poor"

    else:
        return "Severe"


# ============================================================
# AI SUMMARY
# ============================================================

def generate_summary(current_aqi, weather):
    """
    Generate AI environmental summary.
    """

    summary = []

    if current_aqi <= 50:

        summary.append(
            "Air quality is currently excellent."
        )

    elif current_aqi <= 100:

        summary.append(
            "Air quality is acceptable for most people."
        )

    elif current_aqi <= 150:

        summary.append(
            "Sensitive groups should limit outdoor exposure."
        )

    elif current_aqi <= 200:

        summary.append(
            "Air pollution is high. Reduce outdoor activity."
        )

    else:

        summary.append(
            "Very poor air quality detected. Stay indoors."
        )

    if weather["wind_speed"] < 2:

        summary.append(
            "Low wind speed may trap pollutants."
        )

    if weather["humidity"] > 80:

        summary.append(
            "High humidity may increase discomfort."
        )

    if weather["temperature"] > 35:

        summary.append(
            "High temperatures may increase ozone formation."
        )

    return summary