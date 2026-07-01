import streamlit as st


def render_health_score(aqi):

    if aqi <= 50:
        score = 95
        grade = "Excellent"
        color = "#22C55E"
        bg = "#163D2A"
        tips = [
            "🏃 Outdoor exercise is safe.",
            "😷 Mask not required.",
            "🌳 Excellent environmental conditions."
        ]

    elif aqi <= 100:
        score = 80
        grade = "Good"
        color = "#FACC15"
        bg = "#433B0E"
        tips = [
            "🚶 Outdoor activity is acceptable.",
            "😷 Sensitive people should be careful.",
            "💧 Stay hydrated."
        ]

    elif aqi <= 200:
        score = 60
        grade = "Moderate"
        color = "#FB923C"
        bg = "#4A2A12"
        tips = [
            "😷 Wear an N95 mask outdoors.",
            "🏠 Reduce outdoor exposure.",
            "👶 Protect children & elderly."
        ]

    elif aqi <= 300:
        score = 35
        grade = "Poor"
        color = "#EF4444"
        bg = "#4A1D1D"
        tips = [
            "🚫 Avoid outdoor exercise.",
            "🏠 Stay indoors.",
            "🫁 Use air purifier if available."
        ]

    else:
        score = 15
        grade = "Critical"
        color = "#A855F7"
        bg = "#37164D"
        tips = [
            "⚠️ Health emergency conditions.",
            "🏠 Stay indoors.",
            "😷 Wear N95 if leaving home."
        ]

    st.markdown(
        f"""
<div style="
background:#172338;
padding:24px;
border-radius:18px;
border-left:6px solid {color};
">

<h2 style="
margin-top:0;
color:white;
font-size:30px;
">
❤️ Environmental Health Score
</h2>

<div style="
text-align:center;
margin-top:20px;
">

<div style="
font-size:90px;
font-weight:800;
color:{color};
">
{score}
</div>

<div style="
font-size:28px;
font-weight:700;
color:{color};
margin-top:-12px;
">
{grade}
</div>

</div>

<div style="
margin-top:25px;
height:16px;
background:#2A3448;
border-radius:50px;
overflow:hidden;
">

<div style="
width:{score}%;
height:100%;
background:{color};
">
</div>

</div>

<div style="
display:flex;
justify-content:space-between;
margin-top:8px;
color:#94A3B8;
font-size:14px;
">

<span>Poor</span>
<span>Moderate</span>
<span>Excellent</span>

</div>

<div style="
margin-top:25px;
">

""",
        unsafe_allow_html=True,
    )

    for tip in tips:

        st.markdown(
            f"""
<div style="
background:#1E293B;
padding:14px;
border-radius:12px;
margin-bottom:12px;
color:white;
font-size:17px;
">
{tip}
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
<div style="
margin-top:18px;
background:{bg};
padding:16px;
border-radius:12px;
border:1px solid {color};
">

<div style="
font-size:16px;
color:#CBD5E1;
">
Current AQI
</div>

<div style="
font-size:40px;
font-weight:700;
color:{color};
margin-top:4px;
">
{aqi}
</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )