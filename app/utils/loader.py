"""
============================================================
LOADER FUNCTIONS
AI Powered Urban Air Quality Intelligence
============================================================
"""

import streamlit as st
import pandas as pd
import joblib

from src.air_api import (
    get_live_weather,
    get_live_air_quality
)

# ============================================================
# LOAD CSS
# ============================================================

def load_css():
    """
    Load custom CSS.
    """

    with open("app/style.css", "r", encoding="utf-8") as css_file:

        st.markdown(

            f"<style>{css_file.read()}</style>",

            unsafe_allow_html=True

        )

# ============================================================
# LOAD DATASET
# ============================================================

@st.cache_data
def load_dataset():
    """
    Load historical AQI dataset.
    """

    df = pd.read_csv("data/final_dataset.csv")

    df["Date"] = pd.to_datetime(df["Date"])

    return df

# ============================================================
# LOAD TRAINED MODEL
# ============================================================

@st.cache_resource
def load_model():
    """
    Load trained XGBoost model
    and feature list.
    """

    model = joblib.load(
        "models/aqi_xgboost.pkl"
    )

    model_features = joblib.load(
        "models/model_features.pkl"
    )

    return model, model_features

# ============================================================
# LOAD LIVE WEATHER & AQI
# ============================================================

@st.cache_data(ttl=300)
def load_live_data(city):
    """
    Load live weather and AQI.
    Cache expires every 5 minutes.
    """

    weather = get_live_weather(city)

    air = get_live_air_quality(city)

    return weather, air

# ============================================================
# LOAD ALL DATA
# ============================================================

def initialize_project():
    """
    Initialize project resources.
    """

    load_css()

    df = load_dataset()

    model, model_features = load_model()

    cities = sorted(
        df["City"].unique()
    )

    return (
        df,
        model,
        model_features,
        cities
    )