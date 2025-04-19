from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# from posts.models import Post


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "posts/index.html",
    )


def post(request: HttpRequest, slug: str) -> HttpResponse:
    # post: Post | None = Post.objects.find(slug=slug)

    # if post is None:
    #     raise ValueError()

    return render(request, "posts/post.html", context={"slug": slug})
