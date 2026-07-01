import streamlit as st


def render_weather_cards(weather):

    temp = weather.get("temperature", "--")
    humidity = weather.get("humidity", "--")
    wind = weather.get("wind_speed", "--")
    pressure = weather.get("pressure", "--")
    visibility = weather.get("visibility", "--")

    html = f"""
<style>

.weather-grid {{
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:18px;
    margin-bottom:25px;
}}

.weather-card {{
    background:#172338;
    border:1px solid rgba(255,255,255,.06);
    border-radius:18px;
    padding:18px;
    transition:.25s;
    box-shadow:0 8px 20px rgba(0,0,0,.25);
}}

.weather-card:hover {{
    transform:translateY(-4px);
    border-color:#3B82F6;
}}

.weather-icon {{
    font-size:30px;
    margin-bottom:12px;
}}

.weather-title {{
    color:#94A3B8;
    font-size:13px;
}}

.weather-value {{
    color:white;
    font-size:30px;
    font-weight:700;
    margin-top:6px;
}}

.weather-unit {{
    color:#CBD5E1;
    font-size:15px;
}}

@media(max-width:1200px){{
.weather-grid{{
grid-template-columns:repeat(2,1fr);
}}
}}

</style>

<h2 style="color:white;margin-bottom:18px;">
☁️ Current Weather Conditions
</h2>

<div class="weather-grid">

<div class="weather-card">
<div class="weather-icon">🌡️</div>
<div class="weather-title">Temperature</div>
<div class="weather-value">{temp}<span class="weather-unit"> °C</span></div>
</div>

<div class="weather-card">
<div class="weather-icon">💧</div>
<div class="weather-title">Humidity</div>
<div class="weather-value">{humidity}<span class="weather-unit"> %</span></div>
</div>

<div class="weather-card">
<div class="weather-icon">💨</div>
<div class="weather-title">Wind Speed</div>
<div class="weather-value">{wind}<span class="weather-unit"> km/h</span></div>
</div>

<div class="weather-card">
<div class="weather-icon">🌤️</div>
<div class="weather-title">Pressure</div>
<div class="weather-value">{pressure}<span class="weather-unit"> hPa</span></div>
</div>

<div class="weather-card">
<div class="weather-icon">👁️</div>
<div class="weather-title">Visibility</div>
<div class="weather-value">{visibility}<span class="weather-unit"> km</span></div>
</div>

</div>
"""

    st.markdown(html, unsafe_allow_html=True)