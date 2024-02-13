.. _database_structure:

=============================
Database Structure and Models
=============================

The "P13" project utilizes Django models to define the structure of its database. Below are the key data models used in the project.

Address Model
-------------

The `Address` model represents a physical address and has the following attributes:

- **number:** PositiveIntegerField, The street number.
- **street:** CharField, The street name.
- **city:** CharField, The city name.
- **state:** CharField, The state abbreviation.
- **zip_code:** PositiveIntegerField, The ZIP code.
- **country_iso_code:** CharField, The ISO code of the country.

Letting Model
-------------

The `Letting` model represents a letting (rental) with the following attributes:

- **title:** CharField, The title of the letting.
- **address:** OneToOneField, The associated address for the letting.

User Profile App
~~~~~~~~~~~~~~~~

The `User profile` model in the "profiles" app is related to the default Django `User` model using a OneToOneField. It includes:

- **user:** OneToOneField, The associated Django User.
- **favorite_city:** CharField, The user's favorite city.

Relationships
-------------

- The `Letting` model is related to the `Address` model using a OneToOneField.
- The `Profile` model is related to the default Django `User` model using a OneToOneField.

These models define the core structure of the "P13" database, providing a foundation for storing address information, lettings, and user profiles.