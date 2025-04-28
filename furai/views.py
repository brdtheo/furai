from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from posts.models import Post


def index(request: HttpRequest) -> HttpResponse:
    # Retrieve the latest blog post. If none, hide the section
    latest_post = Post.objects.latest("created_at")

    return render(
        request,
        "furai/index.html",
        context={"latest_post": latest_post},
    )
