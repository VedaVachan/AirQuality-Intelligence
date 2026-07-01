import streamlit as st
import plotly.graph_objects as go


def render_live_aqi_panel(aqi, pollutants):

    # ---------- AQI STATUS ----------
    if aqi <= 50:
        status = "Good"
        color = "#2ECC71"

    elif aqi <= 100:
        status = "Moderate"
        color = "#F1C40F"

    elif aqi <= 200:
        status = "Unhealthy for Sensitive Groups"
        color = "#F39C12"

    elif aqi <= 300:
        status = "Very Unhealthy"
        color = "#E74C3C"

    else:
        status = "Hazardous"
        color = "#8E44AD"

    # ---------- TITLE ----------
    st.subheader("🌍 Live Air Quality")

    col1, col2 = st.columns([1.2, 1])

    # =====================================================
    # LEFT SIDE
    # =====================================================
    with col1:

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=aqi,

            number={
                "font": {
                    "size": 46,
                    "color": "white"
                }
            },

            gauge={
                "axis": {
                    "range": [0, 500]
                },

                "bar": {
                    "color": color,
                    "thickness": 0.35
                },

                "steps": [
                    {"range": [0, 50], "color": "#2ECC71"},
                    {"range": [50, 100], "color": "#F1C40F"},
                    {"range": [100, 200], "color": "#F39C12"},
                    {"range": [200, 300], "color": "#E74C3C"},
                    {"range": [300, 500], "color": "#8E44AD"},
                ],

                "bgcolor": "#172338",

                "borderwidth": 0,
            }
        ))

        fig.update_layout(

            height=350,

            paper_bgcolor="#172338",

            plot_bgcolor="#172338",

            margin=dict(l=15, r=15, t=20, b=15),

            font=dict(color="white")
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displayModeBar": False}
        )

        st.markdown(
    f"### Status: <span style='color:{color}'>{status}</span>",
    unsafe_allow_html=True
)

    # =====================================================
    # RIGHT SIDE
    # =====================================================

    with col2:

        st.subheader("📊 AQI Summary")

        st.metric("Current AQI", int(aqi))

        st.metric("Primary Pollutant", "PM2.5")

        st.metric("Health Risk", status)

        st.divider()

        st.subheader("🌫 Pollutants")

        names = {
            "pm2_5": "PM2.5",
            "pm10": "PM10",
            "no2": "NO₂",
            "so2": "SO₂",
            "co": "CO",
            "o3": "O₃"
        }

        for key, label in names.items():

            value = pollutants.get(key, "--")

            c1, c2 = st.columns([2, 1])

            c1.write(label)

            c2.write(value)

        st.divider()

        st.progress(min(aqi / 500, 1.0))

        st.caption(status)