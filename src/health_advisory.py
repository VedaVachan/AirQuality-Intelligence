def get_health_advisory(aqi):

    if aqi <= 50:
        return """
✅ Good Air Quality

• Safe for outdoor activities
• No health risk
"""

    elif aqi <= 100:
        return """
🟡 Moderate Air Quality

• Acceptable for most people
• Sensitive individuals should limit prolonged exposure
"""

    elif aqi <= 150:
        return """
🟠 Unhealthy for Sensitive Groups

• Children and elderly should reduce outdoor activity
• Consider wearing a mask
"""

    elif aqi <= 200:
        return """
🔴 Poor Air Quality

• Avoid strenuous outdoor exercise
• Wear N95 masks
• Schools should reduce outdoor activities
"""

    else:
        return """
⚫ Very Poor Air Quality

• Stay indoors if possible
• Use air purifiers
• Avoid all outdoor physical activities
"""
