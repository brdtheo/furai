from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render

from blog.models import Post


def index(request: HttpRequest) -> HttpResponse:
    try:
        posts = Post.objects.all()  # TODO: implement proper pagination system
    except Post.DoesNotExist:
        raise Http404

    return render(request, "blog/index.html", context={"posts": posts})


def post(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404

    return render(
        request,
        "blog/post.html",
        context={"title": post.title, "content": post.get_content_html()},
    )
