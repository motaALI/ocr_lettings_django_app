from unittest.mock import patch
from django.test import Client
from django.urls import reverse
from django.template import Template, Context
from pytest import mark
from django.test import TestCase

from tests.factories import AddressFactory, LettingFactory


@mark.django_db
class TestLettingTemplate(TestCase):

    def setUp(self):
        self.client = Client()

    @patch("letting.views.Letting.objects.get")
    def test_letting_details_template(self, mock_letting):
        # Create a Letting instance using the factory
        letting_data = LettingFactory(
            id=1,
            title="1 Evergreen Circle",
            address=AddressFactory(
                number=1,
                street="Ruskin Trail",
                city="Aliquippa",
                state="PA",
                zip_code=15001,
                country_iso_code="USA",
            ),
        )

        # Mock the letting function to return the created letting_data
        mock_letting.return_value = letting_data

        # Use reverse to get the URL for the specified letting_id
        response = self.client.get(reverse("letting", args=[1]))

        # Assert that the response status code is 200
        assert response.status_code == 200
        template = Template(response.content.decode("utf-8"))
        context = Context()
        rendered_content = template.render(context)

        # Assert that the expected content is present in the response
        self.assertContains(
            response,
            f'<h1 class="page-header-ui-title mb-3 display-6">{letting_data.title}</h1>',
        )
        self.assertContains(
            response,
            f"<p>{letting_data.address.number} {letting_data.address.street}</p>",
        )
        self.assertContains(
            response,
            f"<p>{letting_data.address.city}, {letting_data.address.state} {letting_data.address.zip_code}</p>",
        )
        self.assertContains(response, f"<p>{letting_data.address.country_iso_code}</p>")

        self.assertInHTML(
            '<a class="btn fw-500 ms-lg-4 btn-primary px-10" href="/">Home</a>',
            rendered_content,
        )
        self.assertInHTML(
            '<a class="btn fw-500 ms-lg-4 btn-primary px-10" href="/profiles/">Profiles</a>',
            rendered_content,
        )

        # Ensure the letting function was called with the correct arguments
        mock_letting.assert_called_with(id=1)
