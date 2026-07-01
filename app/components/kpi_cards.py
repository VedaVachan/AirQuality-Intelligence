"""
============================================================
KPI CARDS
AI Powered Urban Air Quality Intelligence
============================================================
"""

import streamlit as st

from utils.helpers import get_visibility


# ============================================================
# KPI CARDS
# ============================================================

def render_kpi_cards(current_aqi, weather):

    st.markdown(
    """
    <div class="section-title">
        📊 Live Environmental Overview
    </div>

    <div class="section-description">
        Real-time environmental conditions for the selected city.
    </div>
    """,
    unsafe_allow_html=True
    )

    temperature = weather["temperature"]
    humidity = weather["humidity"]
    wind_speed = weather["wind_speed"]
    pressure = weather["pressure"]

    visibility = get_visibility(current_aqi)

    c1, c2, c3, c4, c5, c6 = st.columns(6)

    # AQI
    with c1:

        st.markdown(f"""
<div class="kpi-card">

<div class="metric-icon">🌫</div>

<div class="card-subtitle">
Current AQI
</div>

<h2>{current_aqi}</h2>

</div>
""", unsafe_allow_html=True)

    # Temperature
    with c2:

        st.markdown(f"""
<div class="kpi-card">

<div class="metric-icon">🌡</div>

<div class="card-subtitle">
Temperature
</div>

<h2>{temperature:.1f}°C</h2>

</div>
""", unsafe_allow_html=True)

    # Humidity
    with c3:

        st.markdown(f"""
<div class="kpi-card">

<div class="metric-icon">💧</div>

<div class="card-subtitle">
Humidity
</div>

<h2>{humidity}%</h2>

</div>
""", unsafe_allow_html=True)

    # Wind
    with c4:

        st.markdown(f"""
<div class="kpi-card">

<div class="metric-icon">💨</div>

<div class="card-subtitle">
Wind Speed
</div>

<h2>{wind_speed:.1f} m/s</h2>

</div>
""", unsafe_allow_html=True)

    # Pressure
    with c5:

        st.markdown(f"""
<div class="kpi-card">

<div class="metric-icon">🧭</div>

<div class="card-subtitle">
Pressure
</div>

<h2>{pressure} hPa</h2>

</div>
""", unsafe_allow_html=True)

    # Visibility
    with c6:

        st.markdown(f"""
<div class="kpi-card">

<div class="metric-icon">👁</div>

<div class="card-subtitle">
Visibility
</div>

<h2>{visibility}</h2>

</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)