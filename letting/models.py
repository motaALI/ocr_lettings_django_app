
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model representing an address.

    :param number: The street number.
    :type number: int

    :param street: The street name.
    :type street: str

    :param city: The city name.
    :type city: str

    :param state: The state abbreviation (2 characters).
    :type state: str

    :param zip_code: The ZIP code.
    :type zip_code: int

    :param country_iso_code: The ISO code of the country (3 characters).
    :type country_iso_code: str

    :return: A string representation of the address.
    :rtype: str
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f'{self.number} {self.street}'

class Letting(models.Model):
    """
    Model representing a letting.

    :param title: The title of the letting.
    :type title: str

    :param address: The address associated with the letting.
    :type address: Address

    :return: A string representation of the letting.
    :rtype: str
    """
    
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title