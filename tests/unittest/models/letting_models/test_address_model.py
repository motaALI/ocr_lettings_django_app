from django.test import TestCase
import pytest

from letting.models import Addres
from tests.factories import AddressFactory


@pytest.mark.django_db

def test_create_address():
    address = Addres(number=123, street="Main St", city="City", state="CA", zip_code=12345, country_iso_code="USA")
    address.save()
    assert address.id is not None

@pytest.mark.django_db
def test_read_address():
    # Create an address
    address = Addres(number=123, street="Main St", city="City", state="CA", zip_code=12345, country_iso_code="USA")
    address.save()

    # Retrieve the address from the database
    retrieved_address = Addres.objects.get(id=address.id)

    assert retrieved_address is not None

@pytest.mark.django_db
def test_update_address():
    # Create an address
    address = Addres(number=123, street="Main St", city="City", state="CA", zip_code=12345, country_iso_code="USA")
    address.save()

    # Update the address
    address.street = "Updated St"
    address.save()

    # Retrieve the updated address from the database
    retrieved_address = Addres.objects.get(id=address.id)

    assert retrieved_address.street == "Updated St"

@pytest.mark.django_db
def test_delete_address():
    # Create an address
    address = Addres(number=123, street="Main St", city="City", state="CA", zip_code=12345, country_iso_code="USA")
    address.save()

    # Delete the address
    address.delete()

    # Try to retrieve the deleted address from the database
    with pytest.raises(Addres.DoesNotExist):
        Addres.objects.get(id=address.id)

class TestAddressModel(TestCase):

    def test_str_method(self):
        # Create an Addres instance using the factory
        address = AddressFactory(number=123, street='Main St', city='City', state='ST', zip_code=12345, country_iso_code='USA')

        # Assert that the __str__ method returns the expected string
        expected_str = '123 Main St'
        self.assertEqual(str(address), expected_str)