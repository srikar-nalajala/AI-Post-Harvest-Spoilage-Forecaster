import requests
import pandas as pd

def get_weather(region="Hyderabad"):
    """
    Fetches LIVE weather data from Open-Meteo for the selected region.
    Returns current temp, humidity, and hourly forecast.
    """
    # Coordinates Mapping
    REGION_COORDS = {
        "Telangana": (17.3850, 78.4867),       # Hyderabad
        "Andhra Pradesh": (16.5062, 80.6480),  # Vijayawada
        "Karnataka": (12.9716, 77.5946),       # Bangalore
        "Maharashtra": (19.0760, 72.8777),     # Mumbai
        "Tamil Nadu": (13.0827, 80.2707)       # Chennai
    }
    
    # Default to Telangana/Hyderabad if not found
    lat, long = REGION_COORDS.get(region, (17.3850, 78.4867))
    
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": long,
        "current": "temperature_2m,relative_humidity_2m",
        "hourly": "relative_humidity_2m",
        "forecast_days": 1,
        "timezone": "auto"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        current = data.get("current", {})
        hourly = data.get("hourly", {})
        
        temp = current.get("temperature_2m", 0)
        humidity = current.get("relative_humidity_2m", 0)
        
        # Prepare hourly data for chart
        hourly_df = pd.DataFrame({
            "Time": pd.to_datetime(hourly.get("time", [])),
            "Humidity": hourly.get("relative_humidity_2m", [])
        })

        # Determine condition text for display
        if temp > 35:
            condition = "Sunny/Hot"
        elif humidity > 80:
            condition = "Humid/Cloudy"
        else:
            condition = "Clear"

        return {
            "temperature": temp,
            "humidity": humidity,
            "condition": condition,
            "hourly_data": hourly_df,
            "is_live": True
        }

    except Exception as e:
        print(f"Weather API Failed: {e}")
        # Fallback to simple mock if API fails
        return {
            "temperature": 30, 
            "humidity": 60, 
            "condition": "Check Connection",
            "hourly_data": pd.DataFrame(),
            "is_live": False
        }
