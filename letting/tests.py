# from django.test import TestCase
# import pytest
# from django.core.exceptions import ValidationError
# from letting.models import Address, Letting

# class TestLetting(TestCase):
#     @pytest.mark.django_db
#     def test_create_address():
#         address = Address(number=123, street="Main St", city="City", state="CA", zip_code=12345, country_iso_code="USA")
#         address.save()
#         assert address.id is not None

#     @pytest.mark.django_db
#     def test_create_letting():
#         address = Address(number=123, street="Main St", city="City", state="CA", zip_code=12345, country_iso_code="USA")
#         address.save()
#         letting = Letting(title="Nice House", address=address)
#         letting.save()
#         assert letting.id is not None

#     @pytest.mark.django_db
#     def test_address_max_value_validator():
#         with pytest.raises(ValidationError):
#             Address(number=10000, street="Main St", city="City", state="CA", zip_code=12345, country_iso_code="USA").full_clean()

# Similar tests can be written for other validators and scenarios

