from datetime import datetime, timezone

from django.db import models


class Post(models.Model):
    """A representation of a blog post"""

    # Fields
    slug = models.CharField(
        help_text="The URI encoded post title",
        max_length=60,
        unique=True,
    )
    title = models.CharField(
        help_text="The post title, describing the global topic",
        max_length=60,
    )
    content = models.TextField(
        help_text="The post body/content, containing rich text for Markdown display"
    )
    created_at = models.DateTimeField(
        help_text="The creation date of the post", default=datetime.now(timezone.utc)
    )
    updated_at = models.DateTimeField(
        help_text="The most recent update date of the post", null=True, auto_now=True
    )

    # Methods
    def __str__(self) -> str:
        return self.title
