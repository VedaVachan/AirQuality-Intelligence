import streamlit as st


def render_action_cards(current_aqi, predicted_aqi):

    cards = [
        {
            "icon": "🚦",
            "title": "Traffic Control",
            "desc": "Optimize traffic signals and reduce heavy vehicle movement in high pollution zones.",
            "badge": "Recommended",
            "color": "#3B82F6",
        },
        {
            "icon": "🏗️",
            "title": "Construction Monitoring",
            "desc": "Deploy inspection teams and enforce dust suppression at construction sites.",
            "badge": "High Priority",
            "color": "#F59E0B",
        },
        {
            "icon": "🏥",
            "title": "Citizen Health",
            "desc": "Notify hospitals, schools and vulnerable citizens about expected AQI changes.",
            "badge": "Public Alert",
            "color": "#22C55E",
        },
        {
            "icon": "🤖",
            "title": "AI Prediction",
            "desc": f"Current AQI : <b>{current_aqi}</b><br>Tomorrow : <b>{predicted_aqi:.0f}</b>",
            "badge": "AI Generated",
            "color": "#8B5CF6",
        },
    ]

    st.markdown(
        """
<h2 style="
color:white;
font-size:34px;
margin-bottom:22px;
">
🚀 Smart Action Center
</h2>
""",
        unsafe_allow_html=True,
    )

    cols = st.columns(4)

    for col, card in zip(cols, cards):

        with col:

            st.markdown(
                f"""
<div style="
background:#172338;
padding:22px;
border-radius:18px;
border-top:5px solid {card["color"]};
height:320px;
display:flex;
flex-direction:column;
justify-content:space-between;
box-shadow:0 6px 18px rgba(0,0,0,.25);
">

<div>

<div style="
font-size:42px;
margin-bottom:14px;
">
{card["icon"]}
</div>

<div style="
font-size:24px;
font-weight:700;
color:white;
margin-bottom:14px;
">
{card["title"]}
</div>

<div style="
font-size:16px;
line-height:1.7;
color:#CBD5E1;
">
{card["desc"]}
</div>

</div>

<div style="
margin-top:22px;
">

<span style="
background:{card["color"]}22;
color:{card["color"]};
padding:8px 16px;
border-radius:999px;
font-weight:700;
font-size:14px;
">
{card["badge"]}
</span>

</div>

</div>
""",
                unsafe_allow_html=True,
            )