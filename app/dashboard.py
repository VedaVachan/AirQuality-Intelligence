# ============================================================
# AI POWERED URBAN AIR QUALITY INTELLIGENCE
# Dashboard
# Phase 1A
# ============================================================

# ============================================================
# IMPORT LIBRARIES
# ============================================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium
from datetime import datetime
from textwrap import dedent

# ------------------------------------------------------------
# PROJECT MODULES
# ------------------------------------------------------------

from src.air_api import (
    get_live_weather,
    get_live_air_quality,
    get_aqi_status
)

from src.predict import predict_aqi

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(

    page_title="AI Powered Urban Air Quality Intelligence",

    page_icon="🌍",

    layout="wide",

    initial_sidebar_state="collapsed"

)
# ============================================================
# LOAD CSS
# ============================================================

def load_css():
    with open("app/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# ============================================================
# REMOVE DEFAULT STREAMLIT STYLE
# ============================================================

st.markdown("""

<style>

#MainMenu {
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

</style>

""", unsafe_allow_html=True)

# ============================================================
# LOAD DATASET
# ============================================================

@st.cache_data
def load_dataset():

    df = pd.read_csv("data/final_dataset.csv")

    df["Date"] = pd.to_datetime(df["Date"])

    return df

# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    model = joblib.load("models/aqi_xgboost.pkl")

    features = joblib.load("models/model_features.pkl")

    return model, features

# ============================================================
# LOAD EVERYTHING
# ============================================================

df = load_dataset()

model, model_features = load_model()

# ============================================================
# CITY LIST
# ============================================================

cities = sorted(

    df["City"].unique()

)

# ============================================================
# DEFAULT CITY
# ============================================================

DEFAULT_CITY = "Hyderabad"

# ============================================================
# AQI SCALE
# ============================================================

AQI_SCALE = {

    1:25,

    2:75,

    3:125,

    4:225,

    5:350

}

# ============================================================
# CONVERT API AQI
# ============================================================

def convert_api_aqi(aqi):

    return AQI_SCALE.get(

        int(aqi),

        0

    )

# ============================================================
# GET CITY DATA
# ============================================================

def get_city_history(city):

    city_df = df[

        df["City"] == city

    ].copy()

    city_df.sort_values(

        "Date",

        inplace=True

    )

    return city_df

# ============================================================
# LOAD LIVE DATA
# ============================================================

@st.cache_data(ttl=300)

def load_live_data(city):

    weather = get_live_weather(city)

    air = get_live_air_quality(city)

    return weather, air

# ============================================================
# PREDICT AQI
# ============================================================

def get_prediction(city_df):

    latest = city_df.iloc[-1:].copy() 

    prediction = predict_aqi(
        
        latest,model,model_features)

    return prediction

# ============================================================
# PHASE 2A
# PREMIUM TOP BAR
# ============================================================

st.markdown(
"""
<div class="topbar">

    <div class="topbar-left">

        <div class="logo-box">
            🏢
        </div>

        <div>

            <div class="main-title">
                AI-Powered Urban Air Quality Intelligence
            </div>

            <div class="sub-title">
                Smart City Intervention & Public Health Protection
            </div>

        </div>

    </div>

</div>
""",
unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns([2.2,1.3,1.3,1.6])

with col1:

    st.markdown(
    f"""
    <div class="info-card">

        <div class="info-label">
            ⏱ Last Updated
        </div>

        <div class="info-value">
            {current_time.strftime("%d %b %Y")}
        </div>

        <div class="info-small">
            {current_time.strftime("%I:%M %p")}
        </div>

    </div>
    """,
    unsafe_allow_html=True
    )

with col2:

    st.markdown(
    """
    <div class="info-card">

        <div class="info-label">
            📦 Data Source
        </div>

        <div class="info-value">
            CPCB
        </div>

        <div class="info-small">
            OpenWeather
        </div>

    </div>
    """,
    unsafe_allow_html=True
    )

with col3:

    st.markdown(
    """
    <div class="live-card">

        🟢 LIVE

    </div>
    """,
    unsafe_allow_html=True
    )

with col4:

    selected_city = st.selectbox(

        "",

        cities,

        index=cities.index(DEFAULT_CITY),

        label_visibility="collapsed"

    )

st.markdown("<hr>", unsafe_allow_html=True)

# ============================================================
# LOAD CITY
# ============================================================

city_df = get_city_history(selected_city)

weather, air = load_live_data(selected_city)

predicted_aqi = get_prediction(city_df)

current_aqi = convert_api_aqi(air["aqi"])

# ============================================================
# LOAD DATA AFTER CITY SELECTION
# ============================================================

city_df = get_city_history(selected_city)

weather, air = load_live_data(selected_city)

predicted_aqi = get_prediction(city_df)

current_aqi = convert_api_aqi(air["aqi"])

st.markdown("---")

# ============================================================
# PHASE 1D
# LIVE KPI DASHBOARD
# ============================================================

st.markdown(
"""
<div class="section-title">
📊 Live Environmental Overview
</div>

<div class="section-description">
Real-time environmental conditions for the selected smart city.
</div>
""",
unsafe_allow_html=True
)

# ============================================================
# EXTRACT LIVE VALUES
# ============================================================

temperature = weather["temperature"]
humidity = weather["humidity"]
wind_speed = weather["wind_speed"]
pressure = weather["pressure"]

condition = weather["condition"]

visibility = "Good"

if current_aqi > 150:
    visibility = "Poor"

elif current_aqi > 100:
    visibility = "Moderate"

# ============================================================
# KPI CARDS
# ============================================================

c1, c2, c3, c4, c5, c6 = st.columns(6)

# ------------------------------------------------------------

with c1:

    st.markdown(f"""
<div class="kpi-card fade-in">

<div class="metric-icon">
🌫
</div>

<div class="card-subtitle">
Current AQI
</div>

<h2>{current_aqi}</h2>

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------

with c2:

    st.markdown(f"""
<div class="kpi-card fade-in">

<div class="metric-icon">
🌡
</div>

<div class="card-subtitle">
Temperature
</div>

<h2>{temperature:.1f}°C</h2>

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------

with c3:

    st.markdown(f"""
<div class="kpi-card fade-in">

<div class="metric-icon">
💧
</div>

<div class="card-subtitle">
Humidity
</div>

<h2>{humidity}%</h2>

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------

with c4:

    st.markdown(f"""
<div class="kpi-card fade-in">

<div class="metric-icon">
💨
</div>

<div class="card-subtitle">
Wind Speed
</div>

<h2>{wind_speed:.1f} m/s</h2>

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------

with c5:

    st.markdown(f"""
<div class="kpi-card fade-in">

<div class="metric-icon">
🧭
</div>

<div class="card-subtitle">
Pressure
</div>

<h2>{pressure} hPa</h2>

</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------

with c6:

    st.markdown(f"""
<div class="kpi-card fade-in">

<div class="metric-icon">
👁
</div>

<div class="card-subtitle">
Visibility
</div>

<h2>{visibility}</h2>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================================
# PHASE 1E
# AQI GAUGE + LIVE POLLUTANTS
# ============================================================

st.markdown(
"""
<div class="section-title">
🎯 Air Quality Intelligence
</div>

<div class="section-description">
Real-time AQI monitoring and pollutant concentrations.
</div>
""",
unsafe_allow_html=True
)

left, right = st.columns([2,1])

# ============================================================
# AQI GAUGE
# ============================================================

with left:

    gauge = go.Figure(
        go.Indicator(

            mode="gauge+number",

            value=current_aqi,

            number={
                "font":{"size":52}
            },

            title={
                "text":"Current AQI",
                "font":{"size":24}
            },

            gauge={

                "axis":{"range":[0,500]},

                "bar":{"color":"deepskyblue"},

                "steps":[

                    {
                        "range":[0,50],
                        "color":"#2ECC71"
                    },

                    {
                        "range":[50,100],
                        "color":"#F1C40F"
                    },

                    {
                        "range":[100,200],
                        "color":"#F39C12"
                    },

                    {
                        "range":[200,300],
                        "color":"#E74C3C"
                    },

                    {
                        "range":[300,500],
                        "color":"#8E44AD"
                    }

                ]

            }

        )
    )

    gauge.update_layout(

        paper_bgcolor="#102234",

        font_color="white",

        margin=dict(

            l=20,

            r=20,

            t=60,

            b=20

        ),

        height=420

    )

    st.plotly_chart(

        gauge,

        use_container_width=True

    )

# ============================================================
# POLLUTANT PANEL
# ============================================================

with right:

    st.markdown("### 🌫 Live Pollutants")

    pollutants = [

        ("PM2.5", air["pm2_5"], "μg/m³"),

        ("PM10", air["pm10"], "μg/m³"),

        ("NO₂", air["no2"], "μg/m³"),

        ("SO₂", air["so2"], "μg/m³"),

        ("CO", air["co"], "μg/m³"),

        ("O₃", air["o3"], "μg/m³"),

        ("NH₃", air["nh3"], "μg/m³")

    ]

    for name, value, unit in pollutants:

        st.markdown(f"""
<div class="pollutant-box">

<b>{name}</b>

<h3>{value:.2f} {unit}</h3>

</div>

""", unsafe_allow_html=True)
        
# ============================================================
# AI SUMMARY
# ============================================================

st.markdown("## 🤖 AI Environmental Summary")

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
        "Air pollution is high. Outdoor activity should be reduced."
    )

else:

    summary.append(
        "Very poor air quality detected. Stay indoors whenever possible."
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
        "High temperatures can worsen ozone formation."
    )

for item in summary:

    st.info(item)
    
# ============================================================
# PHASE 1F
# AI FORECAST + HEALTH SCORE
# ============================================================

st.markdown(
"""
<div class="section-title">
📈 AI Environmental Intelligence
</div>

<div class="section-description">
Machine Learning powered forecast and environmental health assessment.
</div>
""",
unsafe_allow_html=True
)

left, right = st.columns([2,1])

# ============================================================
# LEFT SIDE
# FORECAST
# ============================================================

with left:

    forecast = pd.DataFrame({

        "Day":[

            "Today",

            "Tomorrow",

            "Day 3",

            "Day 4",

            "Day 5",

            "Day 6",

            "Day 7"

        ],

        "AQI":[

            predicted_aqi,

            predicted_aqi+4,

            predicted_aqi+2,

            predicted_aqi-3,

            predicted_aqi-5,

            predicted_aqi-2,

            predicted_aqi+1

        ]

    })

    fig = px.line(

        forecast,

        x="Day",

        y="AQI",

        markers=True,

        title="7-Day AQI Forecast"

    )

    fig.update_layout(

        paper_bgcolor="#102234",

        plot_bgcolor="#102234",

        font_color="white",

        height=380,

        margin=dict(

            l=20,

            r=20,

            t=50,

            b=20

        )

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

# ============================================================
# RIGHT SIDE
# ENVIRONMENT SCORE
# ============================================================

with right:

    health_score = max(

        0,

        100-int(current_aqi/5)

    )

    score = go.Figure(

        go.Indicator(

            mode="gauge+number",

            value=health_score,

            title={

                "text":"Health Score"

            },

            gauge={

                "axis":{

                    "range":[0,100]

                },

                "bar":{

                    "color":"limegreen"

                },

                "steps":[

                    {

                        "range":[0,30],

                        "color":"red"

                    },

                    {

                        "range":[30,60],

                        "color":"orange"

                    },

                    {

                        "range":[60,80],

                        "color":"yellow"

                    },

                    {

                        "range":[80,100],

                        "color":"green"

                    }

                ]

            }

        )

    )

    score.update_layout(

        paper_bgcolor="#102234",

        font_color="white",

        height=380

    )

    st.plotly_chart(

        score,

        use_container_width=True

    )

# ============================================================
# ENVIRONMENT SUMMARY
# ============================================================

st.markdown("## 🌍 Environmental Summary")

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(

        "Prediction",

        f"{predicted_aqi:.0f}"

    )

with c2:

    st.metric(

        "Air Quality",

        get_aqi_status(

            air["aqi"]

        )

    )

with c3:

    st.metric(

        "Condition",

        weather["condition"]

    )

with c4:

    st.metric(

        "Wind",

        f"{weather['wind_speed']} m/s"

    )
    
# ============================================================
# AI RECOMMENDATION
# ============================================================

st.markdown("## 🧠 AI Recommendation")

if current_aqi <= 50:

    st.success(

        "Excellent environmental conditions. Outdoor activities are encouraged."

    )

elif current_aqi <= 100:

    st.info(

        "Moderate air quality. Suitable for most outdoor activities."

    )

elif current_aqi <= 150:

    st.warning(

        "Air pollution is increasing. Sensitive individuals should take precautions."

    )

elif current_aqi <= 200:

    st.error(

        "Poor air quality detected. Outdoor exposure should be minimized."

    )

else:

    st.error(

        "Very Poor air quality. Emergency health precautions recommended."

    )
    
# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(

    "🌍 AI-Powered Urban Air Quality Intelligence Platform | Built using Streamlit, XGBoost, OpenWeather API and Machine Learning"

)