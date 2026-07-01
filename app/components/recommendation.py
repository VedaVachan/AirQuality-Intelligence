import streamlit as st


def render_recommendation(predicted_aqi):

    if predicted_aqi <= 50:
        color = "#22C55E"
        bg = "#163D2A"
        level = "🟢 Good"
        tips = [
            "Enjoy outdoor activities.",
            "Windows can remain open.",
            "Walking and cycling are recommended.",
            "No mask required."
        ]

    elif predicted_aqi <= 100:
        color = "#FACC15"
        bg = "#3E3714"
        level = "🟡 Moderate"
        tips = [
            "Sensitive people should limit long outdoor activity.",
            "Prefer parks over busy roads.",
            "Stay hydrated.",
            "Monitor AQI regularly."
        ]

    elif predicted_aqi <= 200:
        color = "#FB923C"
        bg = "#472A15"
        level = "🟠 Unhealthy"
        tips = [
            "Reduce outdoor exposure.",
            "Wear an N95 mask.",
            "Avoid jogging near traffic.",
            "Use an air purifier indoors."
        ]

    elif predicted_aqi <= 300:
        color = "#EF4444"
        bg = "#4A1D1D"
        level = "🔴 Very Unhealthy"
        tips = [
            "Avoid outdoor exercise.",
            "Children and elderly should stay indoors.",
            "Close windows.",
            "Use air purification."
        ]

    else:
        color = "#A855F7"
        bg = "#37164D"
        level = "🟣 Hazardous"
        tips = [
            "Stay indoors.",
            "Wear N95 if outside.",
            "Avoid unnecessary travel.",
            "Follow government advisories."
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
💡 AI Recommendations
</h2>

<div style="
background:{bg};
padding:14px;
border-radius:12px;
margin-top:15px;
margin-bottom:20px;
color:{color};
font-size:22px;
font-weight:700;
text-align:center;
">
{level}
</div>

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
display:flex;
align-items:center;
color:white;
font-size:17px;
">
✅&nbsp;&nbsp;{tip}
</div>
""",
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
<div style="
margin-top:18px;
padding:16px;
border-radius:12px;
background:#0F172A;
border:1px solid {color};
text-align:center;
">

<div style="
color:#94A3B8;
font-size:15px;
">
Predicted AQI
</div>

<div style="
font-size:42px;
font-weight:700;
color:{color};
margin-top:6px;
">
{predicted_aqi:.0f}
</div>

</div>

</div>
""",
        unsafe_allow_html=True,
    )