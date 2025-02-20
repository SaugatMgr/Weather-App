from django.urls import path

from apps.weather.views import weather_by_city, index

urlpatterns = [
    path("", index, name="index"),
    path("search/", weather_by_city, name="weather_by_city"),
]
