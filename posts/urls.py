from django.urls import URLPattern, URLResolver, path

from .views import index

urlpatterns: list[URLResolver | URLPattern] = [
    path("", index),
]
