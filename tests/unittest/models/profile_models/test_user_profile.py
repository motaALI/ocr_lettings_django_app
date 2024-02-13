from django.test import TestCase
import pytest
from tests.factories import UserFactory, ProfileFactory
from django.contrib.auth.models import User
from user_profile.models import Profile


@pytest.mark.django_db
def test_create_profile():
    user = UserFactory()
    profile = ProfileFactory(user=user, favorite_city="Test City")
    assert profile.id is not None

@pytest.mark.django_db
def test_read_profile():
    profile = ProfileFactory()
    retrieved_profile = Profile.objects.get(id=profile.id)
    assert retrieved_profile is not None

@pytest.mark.django_db
def test_update_profile():
    profile = ProfileFactory()
    profile.favorite_city = "Updated City"
    profile.save()
    retrieved_profile = Profile.objects.get(id=profile.id)
    assert retrieved_profile.favorite_city == "Updated City"

@pytest.mark.django_db
def test_delete_profile():
    profile = ProfileFactory()
    profile.delete()
    with pytest.raises(Profile.DoesNotExist):
        Profile.objects.get(id=profile.id)
        
class TestStrProfileModel(TestCase):
    def test_str_method(self):
            # Create a user and profile using the factories
            user = UserFactory(username='testuser')
            profile = ProfileFactory(user=user, favorite_city='Test City')

            # Assert that the __str__ method returns the expected string
            expected_str = 'testuser'
            self.assertEqual(str(profile), expected_str)