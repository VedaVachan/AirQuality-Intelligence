import streamlit as st


def render_header(cities, default_city, current_time):

    left, right = st.columns([7.2, 1.6], gap="small")

    with left:

        st.markdown(f"""
<div class="header-card">

<div class="header-title-row">

<div class="header-title">
🌍 AI-Powered Urban Air Quality Intelligence
</div>

</div>

<div class="header-subtitle">
Smart City Intervention &amp; Public Health Protection
</div>

<div class="header-divider"></div>

<div class="header-bottom">

<div class="header-item">
🕒 {current_time.strftime("%d %b %Y • %I:%M %p")}
</div>

<div class="header-item">
📡 OpenWeather + CPCB
</div>

<div class="header-item live">
<span class="live-dot"></span>
LIVE MONITORING
</div>

</div>

</div>
""", unsafe_allow_html=True)

    with right:

        st.markdown("""
<div class="city-label">
📍 Select City
</div>
""", unsafe_allow_html=True)

        city = st.selectbox(
            "",
            cities,
            index=cities.index(default_city),
            key="city_select",
            label_visibility="collapsed"
        )

    return city