from django.urls import URLPattern, URLResolver, path

from .views import index, post

urlpatterns: list[URLResolver | URLPattern] = [
    path("", index, name="posts"),
    path("<str:slug>", post, name="post"),
]
