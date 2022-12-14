from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, User, Category
from django.contrib import auth


client = Client()


class TestViews(TestCase):
    def setup(self):
        self.user = User.objects.create_user(
            username="usertest500", password="yhwkWuQQ_94_yTTop."
        )

        login = self.client.login(username="usertest500", password="yhwkWuQQ_94_yTTop.")

        Post.objects.create(
            title="Test post",
            content="This is test post",
            slug="test-post",
            image="image.svg",
            category=Category.objects.create(),
        )

        self.assertTrue(login)

    def test_homepage_url(self):
        response = self.client.get(reverse("blog:homepage"))
        self.assertEqual(response.status_code, 200)

    def test_go_to_post_details_page(self):
        TestViews.setup(self)

        post = Post.objects.get(slug="test-post")

        response = self.client.post(reverse("blog:post_details", args=(post.slug,)))
        self.assertEqual(response.status_code, 200)

    def test_go_to_add_post_section(self):
        TestViews.setup(self)

        response = self.client.post(reverse("blog:create_post"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="blog/create_post.html")

    def test_view_log_in_page(self):
        response = self.client.get(reverse("blog:login_user"))

        self.assertEqual(response.status_code, 200)

    def test_log_in(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        data = {
            "username": "testuser",
            "password": "testpassword",
        }

        response = self.client.post(reverse("blog:login_user"), data)

        self.client.login(username="testuser", password="testpassword")

        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

        self.assertEqual(response.status_code, 302)

    def test_log_out(self):
        response = self.client.post(
            "/logout/", {"username": "testuser", "password": "testpassword"}
        )
        self.assertEqual(response.status_code, 302)

    def test_display_categories(self):
        response = self.client.get("/category/")
        self.assertEqual(response.status_code, 200)

    def test_category_details(self):
        TestViews.setup(self)
        category = Category.objects.create(name="Django")

        response = self.client.post(
            reverse("blog:category_details", args=(category.name,))
        )
        self.assertEqual(response.status_code, 200)
