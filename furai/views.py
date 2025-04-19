from datetime import datetime, timezone

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "furai/index.html",
        context={"date": datetime.now(timezone.utc)},
    )
