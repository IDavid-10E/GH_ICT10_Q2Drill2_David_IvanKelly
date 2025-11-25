def run_weather():
    weather_today = {
        "location": "Manila",
        "temperature_c": 32,
        "humidity": 78,
        "condition": "Sunny"
    }

    print(weather_today)
    print(weather_today["temperature_c"])

    weather_today["condition"] = "Cloudy"
    weather_today["heat_index"] = 38

    print(weather_today)
