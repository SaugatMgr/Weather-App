from django.urls import path

from apps.weather.api.v1.views.views import get_weather_data

urlpatterns = [
    path("weather/", get_weather_data, name="weather"),
]
