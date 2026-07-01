import streamlit as st
import folium
from streamlit_folium import st_folium


# -------------------------------------------------
# SAMPLE CITY DATA
# -------------------------------------------------

CITIES = [
    {
        "city": "Delhi",
        "lat": 28.6139,
        "lon": 77.2090,
        "aqi": 218
    },
    {
        "city": "Mumbai",
        "lat": 19.0760,
        "lon": 72.8777,
        "aqi": 156
    },
    {
        "city": "Hyderabad",
        "lat": 17.3850,
        "lon": 78.4867,
        "aqi": 132
    },
    {
        "city": "Chennai",
        "lat": 13.0827,
        "lon": 80.2707,
        "aqi": 91
    },
    {
        "city": "Bengaluru",
        "lat": 12.9716,
        "lon": 77.5946,
        "aqi": 84
    },
    {
        "city": "Kolkata",
        "lat": 22.5726,
        "lon": 88.3639,
        "aqi": 176
    }
]


# -------------------------------------------------
# AQI COLOR
# -------------------------------------------------

def get_color(aqi):

    if aqi <= 50:
        return "green"

    elif aqi <= 100:
        return "lightgreen"

    elif aqi <= 150:
        return "orange"

    elif aqi <= 200:
        return "red"

    elif aqi <= 300:
        return "darkred"

    return "purple"


# -------------------------------------------------
# MAP
# -------------------------------------------------

def render_india_map(selected_city):

    st.markdown(
        """
        <h3 style='color:white;margin-bottom:15px;'>
        🗺 Smart City Air Quality Map
        </h3>
        """,
        unsafe_allow_html=True
    )

    india = folium.Map(

        location=[22.5,79],

        zoom_start=5,

        tiles="CartoDB Positron"

    )

    for city in CITIES:

        popup = f"""
        <b>{city['city']}</b><br>
        AQI : {city['aqi']}
        """

        if city["city"] == selected_city:

            radius = 18

        else:

            radius = 12

        folium.CircleMarker(

            location=[city["lat"],city["lon"]],

            radius=radius,

            popup=popup,

            tooltip=city["city"],

            color=get_color(city["aqi"]),

            fill=True,

            fill_color=get_color(city["aqi"]),

            fill_opacity=0.85

        ).add_to(india)

    st_folium(

        india,

        width=None,

        height=520,

        returned_objects=[]

    )