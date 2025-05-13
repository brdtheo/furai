from django.urls import URLPattern, URLResolver, path

from .views import index, post

urlpatterns: list[URLResolver | URLPattern] = [
    path("", index, name="blog"),
    path("<str:slug>", post, name="blog-post"),
]
