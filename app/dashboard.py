import streamlit as st
from datetime import datetime

from utils.loader import initialize_project, load_live_data
from utils.helpers import (
    convert_api_aqi,
    get_city_history,
    get_prediction,
)
from utils.constants import DEFAULT_CITY

from components.header import render_header
from components.weather_cards import render_weather_cards
from components.live_aqi_panel import render_live_aqi
from components.india_map import render_india_map
from components.forecast_panel import render_forecast_panel
from components.alert_panel import render_alert_panel
from components.trend_chart import render_trend
from components.recommendation import render_recommendation
from components.health_score import render_health_score
from components.action_cards import render_action_cards
from components.footer import render_footer


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Powered Urban Air Quality Intelligence",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ==========================================================
# LOAD CSS
# ==========================================================

with open("app/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True,
    )

st.markdown(
    """
<style>

#MainMenu{
    visibility:hidden;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

.block-container{
    max-width:95%;
    padding-top:1rem;
    padding-bottom:1rem;
}

div[data-testid="stVerticalBlock"]{
    gap:0.65rem;
}

</style>
""",
    unsafe_allow_html=True,
)


# ==========================================================
# SPACING HELPER
# ==========================================================

def spacer(height=24):
    st.markdown(
        f"""
        <div style="height:{height}px;"></div>
        """,
        unsafe_allow_html=True,
    )


# ==========================================================
# INITIALIZE
# ==========================================================

df, model, model_features, cities = initialize_project()

current_time = datetime.now()


# ==========================================================
# HEADER
# ==========================================================

selected_city = render_header(
    cities,
    DEFAULT_CITY,
    current_time,
)


# ==========================================================
# LOAD DATA
# ==========================================================

city_df = get_city_history(df, selected_city)

weather, air = load_live_data(selected_city)

predicted_aqi = get_prediction(
    city_df,
    model,
    model_features,
)

current_aqi = convert_api_aqi(
    air.get("aqi", 1)
)


# ==========================================================
# POLLUTANTS
# ==========================================================

components = air.get("components", {})

pollutants = {
    "pm2_5": components.get("pm2_5", "--"),
    "pm10": components.get("pm10", "--"),
    "no2": components.get("no2", "--"),
    "so2": components.get("so2", "--"),
    "co": components.get("co", "--"),
    "o3": components.get("o3", "--"),
}


# ==========================================================
# WEATHER
# ==========================================================

render_weather_cards(weather)

spacer(24)


# ==========================================================
# LIVE AQI + MAP + FORECAST
# ==========================================================

left, center, right = st.columns(
    [1.25, 2.45, 1.25],
    gap="large",
)

with left:

    render_live_aqi(
        current_aqi,
        pollutants,
    )

with center:

    render_india_map(selected_city)

with right:

    render_forecast_panel(
        predicted_aqi
    )

    spacer(18)

    render_alert_panel(
        current_aqi
    )


# ==========================================================
# TREND
# ==========================================================

spacer(28)

render_trend(city_df)


# ==========================================================
# RECOMMENDATION + HEALTH
# ==========================================================

spacer(28)

recommendation_col, health_col = st.columns(
    [1.65, 1],
    gap="large",
)

with recommendation_col:

    render_recommendation(
        predicted_aqi
    )

with health_col:

    render_health_score(
        current_aqi
    )


# ==========================================================
# ACTION CENTER
# ==========================================================

spacer(30)

render_action_cards(
    current_aqi=current_aqi,
    predicted_aqi=predicted_aqi,
)


# ==========================================================
# FOOTER
# ==========================================================

spacer(30)

render_footer()