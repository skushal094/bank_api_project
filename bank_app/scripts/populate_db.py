import csv, os
from django.conf import settings
from bank_app.models import Bank, State, Location, Branch
from django.db import transaction


@transaction.atomic
def run():
    """
    This method will populate the database with the provided csv file's data.
    CSV file: 'bank_branches.csv'
    """
    f_hand = open(os.path.join(settings.BASE_DIR, "bank_app", "scripts", "bank_branches.csv"), encoding="UTF-8")
    f_csv = csv.DictReader(f_hand)
    i = 0
    for row in f_csv:
        bank, created = Bank.objects.get_or_create(name=row['bank_name'])
        state, created = State.objects.get_or_create(name=row['state'])
        location, created = Location.objects.get_or_create(city=row['city'], district=row['district'], state=state)
        branch, created = Branch.objects.get_or_create(
            name=row['branch'],
            bank=bank,
            address=row['address'],
            ifsc_code=row['ifsc'],
            location=location
        )
        i += 1
        if i % 1000 == 0:
            print("Processed", i, "entries")
