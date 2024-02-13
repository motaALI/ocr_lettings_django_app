from django.test import TestCase
import pytest
from django.core.exceptions import ValidationError
from letting.models import Address, Letting
from tests.factories import LettingFactory

@pytest.mark.django_db
def test_create_letting():
    address = Address.objects.create(number=123, street="Main St", city="City", state="CA", zip_code=12345, country_iso_code="USA")
    letting = Letting.objects.create(title="Nice House", address=address)
    assert letting.id is not None

@pytest.mark.django_db
def test_read_letting():
    address = Address.objects.create(number=123, street="Main St", city="City", state="CA", zip_code=12345, country_iso_code="USA")
    letting = Letting.objects.create(title="Nice House", address=address)

    retrieved_letting = Letting.objects.get(id=letting.id)
    assert retrieved_letting is not None

@pytest.mark.django_db
def test_update_letting():
    address = Address.objects.create(number=123, street="Main St", city="City", state="CA", zip_code=12345, country_iso_code="USA")
    letting = Letting.objects.create(title="Nice House", address=address)

    letting.title = "Updated House"
    letting.save()

    retrieved_letting = Letting.objects.get(id=letting.id)
    assert retrieved_letting.title == "Updated House"

@pytest.mark.django_db
def test_delete_letting():
    address = Address.objects.create(number=123, street="Main St", city="City", state="CA", zip_code=12345, country_iso_code="USA")
    letting = Letting.objects.create(title="Nice House", address=address)

    letting.delete()

    with pytest.raises(Letting.DoesNotExist):
        Letting.objects.get(id=letting.id)


class TestLettingModel(TestCase):

    def test_str_method(self):
        # Create a Letting instance using the factory
        letting = LettingFactory(title='Test Title', address__number=456, address__street='Oak St', address__city='Town', address__state='CA', address__zip_code=67890, address__country_iso_code='CAN')

        # Assert that the __str__ method returns the expected string
        expected_str = 'Test Title'
        self.assertEqual(str(letting), expected_str)