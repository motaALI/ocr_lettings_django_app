# # test_templates.py
# from django.test import Client
# import pytest

# @pytest.fixture
# def client():
#     return Client()

# def test_home_template(client):
#     response = client.get('')
#     assert response.status_code == 200
#     assert 'Holiday Homes' in str(response.content)
#     assert 'Welcome to Holiday Homes' in str(response.content)
#     assert 'Profiles' in str(response.content)
#     assert 'Lettings' in str(response.content)
#     assert 'href="{% url \'profiles_index\' %}"' in str(response.content)
#     assert 'href="{% url \'lettings_index\' %}"' in str(response.content)


# test_templates.py
from django.test import Client
from django.test import TestCase
from django.template import Template, Context


class HomeTemplateTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_template(self):
        # Assuming your template is named 'home.html'
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

        # Render the template using the TemplateResponse class
        template = Template(response.content.decode("utf-8"))
        context = Context()
        rendered_content = template.render(context)

        # Check for expected content in the rendered HTML
        self.assertInHTML(
            '<a class="btn fw-500 ms-lg-4 btn-primary px-10" href="/profiles/">Profiles</a>',
            rendered_content,
        )
        self.assertInHTML(
            '<a class="btn fw-500 ms-lg-4 btn-primary px-10" href="/lettings/">Lettings</a>',
            rendered_content,
        )
