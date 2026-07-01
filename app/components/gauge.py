import streamlit as st
import plotly.graph_objects as go


# ----------------------------------------
# AQI Category
# ----------------------------------------

def get_aqi_status(aqi):

    if aqi <= 50:
        return "Good", "#2ECC71"

    elif aqi <= 100:
        return "Moderate", "#F1C40F"

    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups", "#F39C12"

    elif aqi <= 200:
        return "Unhealthy", "#E67E22"

    elif aqi <= 300:
        return "Very Unhealthy", "#E74C3C"

    else:
        return "Hazardous", "#8E44AD"


# ----------------------------------------
# AQI Gauge
# ----------------------------------------

def render_gauge(aqi,
                 pollutant="PM2.5",
                 updated="05:42 PM"):

    status, color = get_aqi_status(aqi)

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

            "shape":"angular",

            "axis":{
                "range":[0,500],
                "tickwidth":1,
                "tickcolor":"#6C7A96"
            },

            "bar":{
                "color":color,
                "thickness":0.28
            },

            "bgcolor":"rgba(0,0,0,0)",

            "borderwidth":0,

            "steps":[

                {"range":[0,50],"color":"#2ECC71"},

                {"range":[50,100],"color":"#F1C40F"},

                {"range":[100,150],"color":"#F39C12"},

                {"range":[150,200],"color":"#E67E22"},

                {"range":[200,300],"color":"#E74C3C"},

                {"range":[300,500],"color":"#8E44AD"}

            ]

        }

    ))

    fig.update_layout(

        height=360,

        margin=dict(
            l=15,
            r=15,
            t=25,
            b=0
        ),

        paper_bgcolor="#121B2B",

        font=dict(
            color="white"
        )

    )

    st.markdown("""
    <style>

    .aqi-card{

        background:linear-gradient(145deg,#151F30,#111826);

        border-radius:24px;

        border:1px solid rgba(255,255,255,.07);

        padding:18px;

        box-shadow:0 10px 35px rgba(0,0,0,.45);

    }

    .aqi-title{

        display:flex;

        justify-content:space-between;

        color:white;

        font-size:20px;

        font-weight:700;

        margin-bottom:5px;

    }

    .live{

        color:#4ADE80;

        font-size:14px;

    }

    .status{

        text-align:center;

        color:#B8C6DB;

        font-size:18px;

        font-weight:600;

        margin-top:-20px;

    }

    .bottom{

        display:flex;

        justify-content:space-between;

        margin-top:15px;

        border-top:1px solid rgba(255,255,255,.08);

        padding-top:15px;

    }

    .label{

        color:#90A3BF;

        font-size:13px;

    }

    .value{

        color:white;

        font-size:18px;

        font-weight:700;

    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="aqi-card">

        <div class="aqi-title">

            <span>🌍 LIVE AIR QUALITY</span>

            <span class="live">● Live</span>

        </div>

    """, unsafe_allow_html=True)

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displayModeBar":False}
    )

    st.markdown(f"""

    <div class="status">

        {status}

    </div>

    <div class="bottom">

        <div>

            <div class="label">

                Primary Pollutant

            </div>

            <div class="value">

                {pollutant}

            </div>

        </div>

        <div>

            <div class="label">

                Last Updated

            </div>

            <div class="value">

                {updated}

            </div>

        </div>

    </div>

    </div>

    """, unsafe_allow_html=True)