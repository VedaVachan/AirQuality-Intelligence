import streamlit as st
from datetime import datetime


def render_footer():

    year = datetime.now().year

    st.markdown(
        f"""
<hr style="
border:0;
height:1px;
background:#334155;
margin-top:25px;
margin-bottom:25px;
">

<div style="
background:#172338;
padding:28px;
border-radius:18px;
border:1px solid #233554;
">

<div style="
text-align:center;
">

<h2 style="
margin:0;
color:white;
font-size:30px;
">
🌍 AI-Powered Urban Air Quality Intelligence
</h2>

<p style="
margin-top:10px;
color:#94A3B8;
font-size:17px;
">
Smart City • Environmental Intelligence • Decision Support System
</p>

</div>

<div style="
display:flex;
justify-content:space-around;
margin-top:30px;
text-align:center;
flex-wrap:wrap;
">

<div style="padding:12px;">
<div style="font-size:32px;">📡</div>
<div style="color:white;font-size:18px;font-weight:600;">
Real-Time AQI
</div>
<div style="color:#94A3B8;">
CPCB + OpenWeather API
</div>
</div>

<div style="padding:12px;">
<div style="font-size:32px;">🤖</div>
<div style="color:white;font-size:18px;font-weight:600;">
AI Prediction
</div>
<div style="color:#94A3B8;">
Machine Learning Model
</div>
</div>

<div style="padding:12px;">
<div style="font-size:32px;">🗺️</div>
<div style="color:white;font-size:18px;font-weight:600;">
Interactive Maps
</div>
<div style="color:#94A3B8;">
Pan India Monitoring
</div>
</div>

<div style="padding:12px;">
<div style="font-size:32px;">❤️</div>
<div style="color:white;font-size:18px;font-weight:600;">
Public Health
</div>
<div style="color:#94A3B8;">
AI Recommendations
</div>
</div>

</div>

<hr style="
border:0;
height:1px;
background:#334155;
margin-top:25px;
margin-bottom:20px;
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
flex-wrap:wrap;
">

<div style="
color:#94A3B8;
font-size:15px;
">
© {year} AI-Powered Urban Air Quality Intelligence
</div>

<div style="
color:#38BDF8;
font-size:15px;
font-weight:600;
">
Made for Smart City Hackathon 🚀
</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )