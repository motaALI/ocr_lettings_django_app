from django.test import Client
from django.test import TestCase
from django.urls import reverse
from django.template import Template, Context


class TestProfileListTemplate(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_profile_template(self):
        response = self.client.get(reverse("profiles_index"))
        self.assertEqual(response.status_code, 200)

        template = Template(response.content.decode("utf-8"))
        context = Context()
        rendered_content = template.render(context)

        # Check if the title is present
        self.assertContains(
            response, '<h1 class="page-header-ui-title mb-3 display-6">Profiles</h1>'
        )

        self.assertInHTML(
            '<a class="btn fw-500 ms-lg-4 btn-primary px-10" href="/lettings/">Lettings</a>',
            rendered_content,
        )
        self.assertInHTML(
            '<a class="btn fw-500 ms-lg-4 btn-primary px-10" href="/">Home</a>',
            rendered_content,
        )
