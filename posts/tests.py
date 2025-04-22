import datetime

from django.test import TestCase

from .models import Post


class PostTest(TestCase):
    def setUp(self):
        Post.objects.create(
            slug="test-post", title="Test Post", content="lorem ipsum dolor sit amet"
        )
        db_post = Post.objects.last()
        if db_post is None:
            self.fail("No existing Post in database")
        self.post = db_post

    def test_slug(self):
        assert type(self.post.slug) is str
        assert self.post.slug == "test-post"

    def test_title(self):
        assert type(self.post.title) is str
        assert self.post.title == "Test Post"

    def test_content(self):
        assert type(self.post.content) is str
        assert self.post.content == "lorem ipsum dolor sit amet"

    def test_created_at(self):
        assert isinstance(self.post.created_at, datetime.date)

    def test_updated_at(self):
        assert self.post.updated_at is None

    def test_get_content_html(self):
        assert type(self.post.get_content_html()) is str
        assert self.post.get_content_html() == "<p>lorem ipsum dolor sit amet</p>"

    def test_update_post(self):
        self.post.title = "Updated title"
        self.post.slug = "updated-title"
        self.post.save()
        assert self.post.title == "Updated title"
        assert self.post.slug == "updated-title"
        assert self.post.updated_at is not None
