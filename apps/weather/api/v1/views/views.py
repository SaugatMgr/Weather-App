import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.conf import settings

from apps.weather.api.v1.serializers.serializers import WeatherSerializer
from utils.helpers import kelvin_to_celsius


@api_view(["GET"])
def get_weather_data(request):
    serializer = WeatherSerializer(data=request.query_params)
    serializer.is_valid(raise_exception=True)
    city = serializer.validated_data.get("city")

    try:
        weather_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={settings.WEATHER_API_KEY}"
        response = requests.get(weather_url)
        weather_data = response.json()

        code = weather_data.get("cod")
        if code == "401":
            return Response(
                {"error": weather_data.get("message")},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if code == "404":
            return Response(
                {"error": "City not found"}, status=status.HTTP_400_BAD_REQUEST
            )

        main_data = weather_data.get("list")[0].get("main")
        city = weather_data.get("city").get("name")
        context = {
            "city": city,
            "temp": kelvin_to_celsius(main_data.get("temp")),
            "feels_like": kelvin_to_celsius(main_data.get("feels_like")),
            "temp_min": kelvin_to_celsius(main_data.get("temp_min")),
            "temp_max": kelvin_to_celsius(main_data.get("temp_max")),
        }
        return Response(context, status=status.HTTP_200_OK)
    except Exception as e:
        print(str(e))
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
