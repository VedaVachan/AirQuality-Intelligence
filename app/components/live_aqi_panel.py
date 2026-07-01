import streamlit as st
import plotly.graph_objects as go


def render_live_aqi(aqi, pollutant):

    # -------------------------
    # AQI Category
    # -------------------------

    if aqi <= 50:
        status = "Good"
        color = "#4ADE80"

    elif aqi <= 100:
        status = "Moderate"
        color = "#FACC15"

    elif aqi <= 150:
        status = "Unhealthy for Sensitive"
        color = "#FB923C"

    elif aqi <= 200:
        status = "Unhealthy"
        color = "#EF4444"

    elif aqi <= 300:
        status = "Very Unhealthy"
        color = "#A855F7"

    else:
        status = "Hazardous"
        color = "#7E22CE"

    # -------------------------
    # Title
    # -------------------------

    st.markdown("""
    <h3 style="
        color:white;
        margin-bottom:12px;
        font-size:22px;
        font-weight:700;
    ">
    🌿 Live Air Quality
    </h3>
    """, unsafe_allow_html=True)

    # -------------------------
    # Gauge
    # -------------------------

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=aqi,

        number={
            "font": {
                "size": 54,
                "color": color
            }
        },

        gauge={

            "axis": {
                "range": [0, 500],
                "tickwidth": 1,
                "tickcolor": "#64748B"
            },

            "bar": {
                "color": color,
                "thickness": 0.32
            },

            "bgcolor": "#1E293B",

            "borderwidth": 0,

            "steps": [

                {"range":[0,50],"color":"#22C55E"},
                {"range":[50,100],"color":"#EAB308"},
                {"range":[100,200],"color":"#F97316"},
                {"range":[200,300],"color":"#EF4444"},
                {"range":[300,500],"color":"#A855F7"}

            ]
        }
    ))

    fig.update_layout(

        height=260,

        margin=dict(l=10,r=10,t=20,b=10),

        paper_bgcolor="#162235",

        font=dict(color="white")

    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar":False}
    )

    # -------------------------
    # Status
    # -------------------------

    st.markdown(f"""
    <div style="
        text-align:center;
        margin-top:-5px;
        margin-bottom:15px;
    ">

    <div style="
        color:{color};
        font-size:34px;
        font-weight:800;
    ">
    {status}
    </div>

    </div>
    """, unsafe_allow_html=True)

    # -------------------------
    # Pollutant
    # -------------------------

    st.markdown(f"""
    <div style="
        background:#1E293B;
        border-radius:14px;
        padding:14px;
        border:1px solid rgba(255,255,255,.05);
    ">

    <div style="
        color:#94A3B8;
        font-size:14px;
    ">
    Primary Pollutant
    </div>

    <div style="
        color:white;
        font-size:28px;
        font-weight:700;
        margin-top:5px;
    ">
    {pollutant}
    </div>

    </div>
    """, unsafe_allow_html=True)

    # -------------------------
    # AQI Description
    # -------------------------

    st.markdown(f"""
    <div style="
        margin-top:14px;
        padding:14px;
        background:#101827;
        border-radius:14px;
        color:#CBD5E1;
        font-size:14px;
        line-height:1.6;
        border-left:4px solid {color};
    ">

    Current AQI : <b>{aqi}</b><br>

    Air Quality Status :
    <span style="color:{color};font-weight:700;">
    {status}
    </span>

    </div>
    """, unsafe_allow_html=True)