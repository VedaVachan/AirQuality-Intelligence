import streamlit as st
from datetime import datetime


def render_header(cities=None, default_city=None, current_time=None):

    if current_time is None:
        current_time = datetime.now()

    current_time = current_time.strftime("%d %b %Y • %I:%M %p")

    if cities is None:
        cities = ["Hyderabad"]

    if default_city is None:
        default_city = cities[0]

    st.markdown(
        """
<style>

.dashboard-header{
    background:linear-gradient(135deg,#162235,#0F172A);
    border:1px solid rgba(255,255,255,.08);
    border-radius:22px;
    padding:22px 26px;
    margin-bottom:25px;
    box-shadow:0 12px 35px rgba(0,0,0,.35);
}

.title{
    color:white;
    font-size:34px;
    font-weight:800;
    margin-bottom:4px;
}

.subtitle{
    color:#94A3B8;
    font-size:15px;
}

.info-box{
    background:#1E293B;
    border-radius:16px;
    padding:12px;
    text-align:center;
    border:1px solid rgba(255,255,255,.06);
}

.info-title{
    color:#94A3B8;
    font-size:12px;
}

.info-value{
    color:white;
    font-size:16px;
    font-weight:700;
    margin-top:5px;
}

</style>
""",
        unsafe_allow_html=True,
    )

    st.markdown('<div class="dashboard-header">', unsafe_allow_html=True)

    left, right = st.columns([3.2, 2])

    with left:

        st.markdown(
            """
<div class="title">
🌍 AI-Powered Urban Air Quality Intelligence
</div>

<div class="subtitle">
Smart City Intervention • Environmental Intelligence • Public Health
</div>
""",
            unsafe_allow_html=True,
        )

    with right:

        c1, c2, c3 = st.columns([1.3, 1.3, 1.8])

        with c1:

            st.markdown(
                f"""
<div class="info-box">

<div class="info-title">
Last Updated
</div>

<div class="info-value">
{current_time}
</div>

</div>
""",
                unsafe_allow_html=True,
            )

        with c2:

            st.markdown(
                """
<div class="info-box">

<div class="info-title">
Data Source
</div>

<div class="info-value">
CPCB<br>Open-Meteo
</div>

</div>
""",
                unsafe_allow_html=True,
            )

        with c3:

            city = st.selectbox(
                "📍 Select City",
                cities,
                index=cities.index(default_city),
                label_visibility="collapsed",
            )

    st.markdown("</div>", unsafe_allow_html=True)

    return city