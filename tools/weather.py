"""Weather tool using Open-Meteo free APIs."""
import requests


def get_weather(location: str) -> str:
    """Return a short current weather summary for the given location (city name).

    Uses Open-Meteo's geocoding API to find coordinates, then fetches current weather.
    """
    try:
        geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
        resp = requests.get(geocode_url, params={"name": location, "count": 1}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        results = data.get("results")
        if not results:
            return f"Location not found: {location}"
        place = results[0]
        lat = place.get("latitude")
        lon = place.get("longitude")
        name = place.get("name")

        weather_url = "https://api.open-meteo.com/v1/forecast"
        wresp = requests.get(weather_url, params={"latitude": lat, "longitude": lon, "current_weather": True}, timeout=10)
        wresp.raise_for_status()
        wdata = wresp.json()
        current = wdata.get("current_weather")
        if not current:
            return f"Weather info unavailable for {name}"
        temp = current.get("temperature")
        wind = current.get("windspeed")
        direction = current.get("winddirection")
        return f"Current weather for {name}: {temp}°C, wind {wind} km/h at {direction}°"
    except Exception as e:
        return f"Error fetching weather: {e}"
