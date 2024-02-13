# myapp/management/commands/migrate_lettings.py
from django.core.management.base import BaseCommand

from letting.models import Address, Letting

class Command(BaseCommand):
    help = 'Migrate data from the old Letting model structure to the new structure'

    def handle(self, *args, **options):
        # Iterate over existing Letting objects
        for old_letting in Letting.objects.all():
            # Create a new Address object with the old Letting's address data
            new_address = Address.objects.create(
                number=old_letting.address.number,
                street=old_letting.address.street,
                city=old_letting.address.city,
                state=old_letting.address.state,
                zip_code=old_letting.address.zip_code,
                country_iso_code=old_letting.address.country_iso_code,
            )

            # Create a new Letting object with the old Letting's title and the new Address
            new_letting = Letting.objects.create(
                title=old_letting.title,
                address=new_address,
            )

            # Display progress
            self.stdout.write(self.style.SUCCESS(f'Migrated Letting: {old_letting.title}'))

        self.stdout.write(self.style.SUCCESS('Migration completed successfully'))
