import requests

API_KEY = "dab3d934bcd3f161840cf38fd88ddbb0"

CITY_COORDINATES = {
    "Ahmedabad": (23.0225,72.5714),
    "Bengaluru": (12.9716,77.5946),
    "Bhopal": (23.2599,77.4126),
    "Bhubaneswar": (20.2961,85.8245),
    "Chandigarh": (30.7333,76.7794),
    "Chennai": (13.0827,80.2707),
    "Coimbatore": (11.0168,76.9558),
    "Delhi": (28.6139,77.2090),
    "Guwahati": (26.1445,91.7362),
    "Hyderabad": (17.3850,78.4867),
    "Indore": (22.7196,75.8577),
    "Jaipur": (26.9124,75.7873),
    "Kanpur": (26.4499,80.3319),
    "Kochi": (9.9312,76.2673),
    "Kolkata": (22.5726,88.3639),
    "Lucknow": (26.8467,80.9462),
    "Mumbai": (19.0760,72.8777),
    "Nagpur": (21.1458,79.0882),
    "Patna": (25.5941,85.1376),
    "Pune": (18.5204,73.8567),
    "Raipur": (21.2514,81.6296),
    "Ranchi": (23.3441,85.3096),
    "Surat": (21.1702,72.8311),
    "Thiruvananthapuram": (8.5241,76.9366),
    "Visakhapatnam": (17.6868,83.2185)
}


def get_live_air_quality(city):

    lat, lon = CITY_COORDINATES[city]

    url = (
        f"https://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={lat}&lon={lon}&appid={API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    air = data["list"][0]

    return {

        "aqi": air["main"]["aqi"],

        "pm2_5": air["components"]["pm2_5"],

        "pm10": air["components"]["pm10"],

        "co": air["components"]["co"],

        "no2": air["components"]["no2"],

        "so2": air["components"]["so2"],

        "o3": air["components"]["o3"]

    }
