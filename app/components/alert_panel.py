import streamlit as st


def render_alert_panel(current_aqi):

    if current_aqi <= 50:

        color = "#22C55E"
        title = "🟢 GOOD"
        priority = "LOW"
        message = "Air quality is healthy. Outdoor activities are safe."

    elif current_aqi <= 100:

        color = "#FACC15"
        title = "🟡 MODERATE"
        priority = "MEDIUM"
        message = "Sensitive people should limit prolonged outdoor activities."

    elif current_aqi <= 200:

        color = "#FB923C"
        title = "🟠 UNHEALTHY"
        priority = "HIGH"
        message = "Wear an N95 mask and reduce outdoor exposure."

    elif current_aqi <= 300:

        color = "#EF4444"
        title = "🔴 VERY UNHEALTHY"
        priority = "VERY HIGH"
        message = "Avoid outdoor activities. Children and elderly should stay indoors."

    else:

        color = "#A855F7"
        title = "🟣 HAZARDOUS"
        priority = "CRITICAL"
        message = "Remain indoors. Follow emergency health advisories."

    html = f"""
<div style="
background:#172338;
border-radius:18px;
padding:20px;
border-left:6px solid {color};
box-shadow:0 10px 20px rgba(0,0,0,.30);
margin-top:10px;
">

<h2 style="
color:white;
margin:0;
font-size:28px;
font-weight:700;
">
🚨 Alert Center
</h2>

<div style="
background:{color}20;
color:{color};
padding:12px;
margin-top:18px;
border-radius:12px;
font-size:20px;
font-weight:bold;
text-align:center;
">
{title}
</div>

<div style="
margin-top:18px;
background:#1E293B;
padding:15px;
border-radius:12px;
">

<p style="
margin:0;
color:#94A3B8;
font-size:13px;
">
CURRENT AQI
</p>

<h1 style="
margin:5px 0;
color:white;
font-size:40px;
">
{current_aqi}
</h1>

</div>

<div style="
display:flex;
justify-content:space-between;
margin-top:15px;
gap:10px;
">

<div style="
flex:1;
background:#1E293B;
padding:15px;
border-radius:12px;
text-align:center;
">

<p style="
margin:0;
color:#94A3B8;
font-size:13px;
">
Priority
</p>

<h3 style="
margin-top:8px;
color:{color};
">
{priority}
</h3>

</div>

<div style="
flex:1;
background:#1E293B;
padding:15px;
border-radius:12px;
text-align:center;
">

<p style="
margin:0;
color:#94A3B8;
font-size:13px;
">
Status
</p>

<h3 style="
margin-top:8px;
color:white;
">
Active
</h3>

</div>

</div>

<div style="
margin-top:18px;
background:#1F2937;
padding:16px;
border-radius:12px;
">

<p style="
margin:0;
color:white;
font-size:15px;
line-height:1.7;
">
💡 {message}
</p>
</div>

</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True
    )