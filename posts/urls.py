from django.urls import URLPattern, URLResolver, path

from .views import index, post

urlpatterns: list[URLResolver | URLPattern] = [
    path("", index),
    path("<str:slug>", post),
]
