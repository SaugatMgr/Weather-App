import requests
from django.shortcuts import render
from django.conf import settings


def kelvin_to_celsius(kelvin):
    kelvin = float(kelvin)
    return f"{round(kelvin - 273.15, 3)} °C"


def get_weather_data_by_city(city):
    try:
        weather_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={settings.WEATHER_API_KEY}"
        response = requests.get(weather_url)
        weather_data = response.json()

        code = weather_data.get("cod")
        if code == "401":
            return {"error": weather_data.get("message")}
        if code == "404":
            return {"error": "City not found"}

        main_data = weather_data.get("list")[0].get("main")
        city = weather_data.get("city").get("name")
        context = {
            "city": city,
            "temp": kelvin_to_celsius(main_data.get("temp")),
            "feels_like": kelvin_to_celsius(main_data.get("feels_like")),
            "temp_min": kelvin_to_celsius(main_data.get("temp_min")),
            "temp_max": kelvin_to_celsius(main_data.get("temp_max")),
        }
        return {"weather_data": context}
    except Exception as e:
        return {"error": str(e)}


def index(request):
    user_location_data = requests.get("https://ipinfo.io/json").json()
    city = user_location_data.get("city")
    context = get_weather_data_by_city(city)
    return render(request, "weather_by_city.html", context)


def weather_by_city(request):
    city = request.GET.get("city")
    if city:
        context = get_weather_data_by_city(city)
        return render(request, "weather_by_city.html", context)
    return render(request, "weather_by_city.html", {"error": "City name missing."})
