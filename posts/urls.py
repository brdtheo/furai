from django.urls import URLPattern, URLResolver, path

from .views import index, post

urlpatterns: list[URLResolver | URLPattern] = [
    path("", index, name="post-list"),
    path("<str:slug>", post, name="post-detail"),
]
