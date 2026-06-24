def get_recommendations(aqi):

    if aqi <= 100:
        return [
            "Continue regular monitoring",
            "Maintain green zones",
            "Promote public transport"
        ]

    elif aqi <= 150:
        return [
            "Inspect construction sites",
            "Increase road cleaning frequency",
            "Monitor industrial emissions"
        ]

    elif aqi <= 200:
        return [
            "Restrict diesel generators",
            "Increase water sprinkling on roads",
            "Inspect pollution hotspots",
            "Issue public health advisories"
        ]

    else:
        return [
            "Emergency pollution control measures",
            "Temporary restriction on high-emission activities",
            "Activate public health response",
            "Continuous monitoring of hotspots"
        ]
