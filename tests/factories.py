
import factory
from factory.django import DjangoModelFactory
# from django.db.models import MaxValueValidator, MinLengthValidator
from django.contrib.auth.models import User

from user_profile.models import Profile

from letting.models import Address, Letting


class AddressFactory(DjangoModelFactory):
    class Meta:
        model = Address

    number = factory.Sequence(lambda n: n)
    street = factory.Faker('street_name')
    city = factory.Faker('city')
    state = factory.Faker('state_abbr')
    zip_code = factory.Sequence(lambda n: n)
    country_iso_code = factory.Faker('country_code')

class LettingFactory(DjangoModelFactory):
    class Meta:
        model = Letting

    title = factory.Faker('sentence', nb_words=3)
    address = factory.SubFactory(AddressFactory)
    

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('user_name')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')

class ProfileFactory(DjangoModelFactory):
    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    favorite_city = factory.Faker('city')
