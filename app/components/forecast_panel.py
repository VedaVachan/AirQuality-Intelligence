import streamlit as st


def render_forecast_panel(predicted_aqi):

    if predicted_aqi <= 50:
        risk = "🟢 Good"
        color = "#2ECC71"

    elif predicted_aqi <= 100:
        risk = "🟡 Moderate"
        color = "#F1C40F"

    elif predicted_aqi <= 200:
        risk = "🟠 Unhealthy"
        color = "#F39C12"

    elif predicted_aqi <= 300:
        risk = "🔴 Very Unhealthy"
        color = "#E74C3C"

    else:
        risk = "🟣 Hazardous"
        color = "#8E44AD"

    st.markdown("## 📈 AQI Forecast")

    st.metric(
        label="Tomorrow AQI",
        value=f"{predicted_aqi:.0f}"
    )

    st.metric(
        label="Risk Level",
        value=risk.replace("🟢", "")
                .replace("🟡", "")
                .replace("🟠", "")
                .replace("🔴", "")
                .replace("🟣", ""))

    st.progress(min(predicted_aqi / 500, 1.0))

    st.markdown(
        f"""
<div style="
background:#172338;
padding:15px;
border-radius:12px;
border-left:5px solid {color};
margin-top:15px;
">

<b style="color:white;">Prediction Summary</b>

<br><br>

<span style="color:#cbd5e1;">
Expected AQI:
</span>

<b style="color:white;">
{predicted_aqi:.0f}
</b>

<br>

<span style="color:#cbd5e1;">
Expected Category:
</span>

<b style="color:{color};">
{risk}
</b>

</div>
""",
        unsafe_allow_html=True,
    )