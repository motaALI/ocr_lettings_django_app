import json
from unittest.mock import patch
from django.test import Client
from django.urls import reverse
from django.template import Template, Context
from pytest import mark
from django.test import TestCase

from user_profile.views import profile
from tests.factories import ProfileFactory, UserFactory

@mark.django_db
class TestProfileTemplate(TestCase):

    def setUp(self):
        self.client = Client()

    @patch('user_profile.views.Profile.objects.get')
    def test_profile_details_template(self, mock_profile):
        # Create a profile instance using the factory
        profile_data = ProfileFactory(
            favorite_city="Buenos Aires",
            user=UserFactory(
                username="dlishmund0",
                first_name="Dlish",
                last_name="Hmund",
                email="afeasley0@slate.com"
            )
        )

        # Mock the profile function to return the created profile_data
        mock_profile.return_value = profile_data

        # Use reverse to get the URL for the specified profile_id
        response = self.client.get(reverse('profile', args=[profile_data.user.username]))

        # Assert that the response status code is 200
        assert response.status_code == 200

        # Assert that the expected content is present in the response
        self.assertContains(response, f'<h1 class="page-header-ui-title mb-3 display-6">{profile_data.user.username}</h1>')
        self.assertContains(response, f'<p><strong>First name :</strong> {profile_data.user.first_name}</p>')
        self.assertContains(response, f'<p><strong>Last name :</strong> {profile_data.user.last_name}</p>')
        self.assertContains(response, f'<p><strong>Email :</strong>{profile_data.user.email}</p>', html=True)

        # Your additional assertions go here
        # self.assertInHTML('<a class="btn fw-500 ms-lg-4 btn-primary px-10" href="/profiles/">Back</a>', response.content.decode('utf-8'))
        self.assertInHTML('<a class="btn fw-500 ms-lg-4 btn-primary px-10" href="/">Home</a>', response.content.decode('utf-8'))
        self.assertInHTML('<a class="btn fw-500 ms-lg-4 btn-primary px-10" href="/lettings/">Lettings</a>', response.content.decode('utf-8'))

        # Ensure the profile function was called with the correct arguments
        mock_profile.assert_called_with(user__username="dlishmund0")
