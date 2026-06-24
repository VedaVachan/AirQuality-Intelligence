import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import folium
import requests
from streamlit_folium import st_folium

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="AI-Powered Urban Air Quality Intelligence",
    page_icon="🌍",
    layout="wide"
)




# ---------------------------
# HEALTH ADVISORY
# ---------------------------

def get_health_advisory(aqi):

    if aqi <= 50:
        return "✅ Good Air Quality - Safe for outdoor activities"

    elif aqi <= 100:
        return "🟡 Moderate Air Quality - Acceptable for most people"

    elif aqi <= 150:
        return "🟠 Unhealthy for Sensitive Groups - Elderly and children should limit exposure"

    elif aqi <= 200:
        return "🔴 Poor Air Quality - Wear masks and avoid outdoor exercise"

    else:
        return "⚫ Very Poor Air Quality - Stay indoors whenever possible"


# ---------------------------
# GOVERNMENT RECOMMENDATIONS
# ---------------------------

def get_recommendations(aqi):

    if aqi <= 100:
        return [
            "Promote public transport",
            "Continue regular monitoring",
            "Maintain green zones"
        ]

    elif aqi <= 150:
        return [
            "Inspect construction sites",
            "Increase road cleaning",
            "Monitor industrial emissions"
        ]

    elif aqi <= 200:
        return [
            "Restrict diesel generators",
            "Increase water sprinkling",
            "Inspect pollution hotspots",
            "Issue public health alerts"
        ]

    else:
        return [
            "Emergency pollution response",
            "Restrict high-emission activities",
            "Continuous hotspot monitoring",
            "City-wide health advisories"
        ]


# ---------------------------
# LIVE WEATHER
# ---------------------------

def get_live_weather():

    API_KEY = "dab3d934bcd3f161840cf38fd88ddbb0"

    city = "Hyderabad"

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    data = response.json()

    return {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "condition": data["weather"][0]["main"]
    }


# ---------------------------
# LOAD DATA
# ---------------------------

df = pd.read_csv("data/final_dataset.csv")

model = joblib.load("models/aqi_xgboost.pkl")

latest = df.iloc[-1]

sample = pd.DataFrame([{
    "temperature": latest["temperature"],
    "rainfall": latest["rainfall"],
    "wind_speed": latest["wind_speed"],
    "month": latest["month"],
    "day_of_year": latest["day_of_year"],
    "aqi_lag1": latest["aqi_lag1"],
    "aqi_7day_avg": latest["aqi_7day_avg"]
}])

predicted_aqi = float(model.predict(sample)[0])

weather = get_live_weather()

# ---------------------------
# TITLE
# ---------------------------

st.title("🌍 AI-Powered Urban Air Quality Intelligence Platform")

st.markdown("---")


# ---------------------------
# SIDEBAR
# ---------------------------

st.sidebar.title("🌍 Air Quality Controls")

selected_city = st.sidebar.selectbox(
    "City",
    ["Hyderabad"]
)

st.sidebar.metric(
    "Predicted AQI",
    int(predicted_aqi)
)

# ---------------------------
# METRICS
# ---------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Current AQI",
        int(latest["aqi"])
    )

with col2:
    st.metric(
        "Predicted AQI",
        int(predicted_aqi)
    )

with col3:
    st.metric(
        "Temperature",
        f"{latest['temperature']} °C"
    )
    
st.subheader("🌦 Live Weather")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Temperature",
        f"{weather['temperature']} °C"
    )

with c2:
    st.metric(
        "Humidity",
        f"{weather['humidity']} %"
    )

with c3:
    st.metric(
        "Wind Speed",
        f"{weather['wind_speed']} m/s"
    )

with c4:
    st.metric(
        "Condition",
        weather['condition']
    )


# ---------------------------
# AQI RISK SCORE
# ---------------------------

st.subheader("🎯 AQI Risk Score")

risk_score = min(int(predicted_aqi / 2), 100)

st.progress(risk_score)

st.metric(
    "Risk Score",
    f"{risk_score}/100"
)


# ---------------------------
# AQI GAUGE
# ---------------------------

import plotly.graph_objects as go

st.subheader("🎯 AQI Gauge")

gauge = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=predicted_aqi,
        title={"text": "AQI"},
        gauge={
            "axis": {"range": [0, 300]},
            "steps": [
                {"range": [0, 50], "color": "green"},
                {"range": [50, 100], "color": "yellow"},
                {"range": [100, 200], "color": "orange"},
                {"range": [200, 300], "color": "red"}
            ]
        }
    )
)

st.plotly_chart(
    gauge,
    use_container_width=True
)


# ---------------------------
# AQI STATUS
# ---------------------------

st.subheader("📊 AQI Status")

if predicted_aqi <= 50:
    st.success("🟢 GOOD")
elif predicted_aqi <= 100:
    st.info("🟡 MODERATE")
elif predicted_aqi <= 200:
    st.warning("🟠 POOR")
else:
    st.error("🔴 VERY POOR")


# ---------------------------
# HEALTH ADVISORY
# ---------------------------

st.subheader("🏥 Citizen Health Advisory")

st.info(
    get_health_advisory(predicted_aqi)
)

# ---------------------------
# SENSITIVE GROUP ALERT
# ---------------------------

st.subheader("👨‍👩‍👧 Sensitive Group Alert")

if predicted_aqi > 150:
    st.error(
        "Children, elderly citizens and asthma patients should stay indoors."
    )

elif predicted_aqi > 100:
    st.warning(
        "Sensitive groups should reduce outdoor activities."
    )

else:
    st.success(
        "Air quality is safe for most people."
    )
    
# ---------------------------
# GOVT RECOMMENDATIONS
# ---------------------------

st.subheader("🏛 Government Recommendations")

for item in get_recommendations(predicted_aqi):
    st.write("•", item)

# ---------------------------
# POLLUTION SOURCE ANALYSIS
# ---------------------------

st.subheader("🏭 Pollution Source Analysis")

source_df = pd.DataFrame({
    "Source": [
        "Traffic",
        "Industry",
        "Construction",
        "Residential"
    ],
    "Contribution": [
        40,
        30,
        20,
        10
    ]
})

source_fig = px.pie(
    source_df,
    names="Source",
    values="Contribution",
    hole=0.4,
    title="Estimated Pollution Sources"
)

st.plotly_chart(
    source_fig,
    use_container_width=True
)

# ---------------------------
# POLLUTION ALERT
# ---------------------------

st.subheader("🚨 Pollution Alert")

if predicted_aqi > 150:
    st.error(
        "High pollution expected. Avoid outdoor activities."
    )

elif predicted_aqi > 100:
    st.warning(
        "Moderate pollution. Sensitive groups should be careful."
    )
    

else:
    st.success(
        "Air quality is acceptable."
    )

# ---------------------------
# DAILY REPORT
# ---------------------------

st.subheader("📄 Daily Air Quality Report")

report = f"""
Date: Latest Available Data

Current AQI: {int(latest['aqi'])}
Predicted AQI: {int(predicted_aqi)}

Temperature: {latest['temperature']} °C
Wind Speed: {latest['wind_speed']} km/h

Recommended Actions:
"""

for item in get_recommendations(predicted_aqi):
    report += f"\n• {item}"

st.text_area(
    "Generated Report",
    report,
    height=220
)

st.download_button(
    label="📥 Download Report",
    data=report,
    file_name="air_quality_report.txt",
    mime="text/plain"
)

# ---------------------------
# AQI TREND
# ---------------------------

st.subheader("📈 AQI Trend")

fig = px.line(
    df.tail(365),
    x="date",
    y="aqi",
    title="AQI Trend (Last 365 Days)"
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.subheader("📅 Next 7-Day AQI Forecast")

forecast_days = pd.DataFrame({
    "Day":[
        "Today",
        "Day 2",
        "Day 3",
        "Day 4",
        "Day 5",
        "Day 6",
        "Day 7"
    ],
    "Forecast AQI":[
        predicted_aqi,
        predicted_aqi+3,
        predicted_aqi+5,
        predicted_aqi+2,
        predicted_aqi-2,
        predicted_aqi-4,
        predicted_aqi-1
    ]
})

forecast_fig = px.line(
    forecast_days,
    x="Day",
    y="Forecast AQI",
    markers=True,
    title="7-Day AQI Forecast"
)

st.plotly_chart(
    forecast_fig,
    width="stretch"
)


# ---------------------------
# WEATHER TREND
# ---------------------------

st.subheader("🌦 Weather Overview")

weather_fig = px.line(
    df.tail(365),
    x="date",
    y=["temperature", "wind_speed"],
    title="Temperature and Wind Speed"
)

st.plotly_chart(
    weather_fig,
    use_container_width=True
)

st.subheader("🚦 AQI Category Distribution")

df["category"] = pd.cut(
    df["aqi"],
    bins=[0,50,100,200,500],
    labels=["Good","Moderate","Poor","Very Poor"]
)

category_counts = df["category"].value_counts()

pie_fig = px.pie(
    values=category_counts.values,
    names=category_counts.index,
    title="AQI Category Distribution"
)

st.plotly_chart(
    pie_fig,
    width="stretch"
)


# ---------------------------
# POLLUTION MAP
# ---------------------------

st.subheader("🗺 Air Quality Monitoring Stations")

try:

    stations = pd.read_csv(
        "data/station_pollution_india.csv"
    )

    stations = stations[
        stations["city"].str.contains(
            "Hyderabad",
            case=False,
            na=False
        )
    ]

    m = folium.Map(
        location=[17.3850, 78.4867],
        zoom_start=10
    )

    for _, row in stations.iterrows():

        try:
            lat = float(row["latitude"])
            lon = float(row["longitude"])

            folium.Marker(
                [lat, lon],
                popup=f"""
                Station: {row['station']}<br>
                Pollutant: {row['pollutant_id']}<br>
                Average Value: {row['pollutant_avg']}
                """
            ).add_to(m)

        except:
            pass

    st_folium(
        m,
        width=1000,
        height=500
    )

except Exception as e:
    st.warning(f"Map Error: {e}")


# ---------------------------
# DATA TABLE
# ---------------------------

st.subheader("🏆 Top 10 Worst Pollution Days")

worst_days = df.nlargest(10, "aqi")

st.dataframe(
    worst_days[["date", "aqi"]],
    width="stretch"
)


st.subheader("📋 Recent AQI Records")

st.dataframe(
    df.tail(10),
    use_container_width=True
)

# ---------------------------
# FOOTER
# ---------------------------

st.success("✅ Dashboard Loaded Successfully")