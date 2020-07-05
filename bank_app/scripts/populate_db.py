import csv, os
from django.conf import settings
from bank_app.models import Bank, State, Location, Branch
from django.db import transaction


def run():
    """
    This method will populate the database with the provided csv file's data.
    CSV file: 'bank_branches.csv'
    """
    f_hand = open(os.path.join(settings.BASE_DIR, "bank_app", "scripts", "bank_branches.csv"), encoding="UTF-8")
    f_csv = csv.DictReader(f_hand)
    bank_set = set()
    state_set = set()
    location_list = list()
    data = []
    for row in f_csv:
        data.append(dict(row))
        bank_set.add(row['bank_name'])
        state_set.add(row['state'])
        location_list.append({
            "city": row['city'],
            "district": row['district'],
            "state": row['state']
        })
    print("File reading complete.")
    print("Starting to save bank names into database.")
    banks = save_banks(bank_set=bank_set)
    print(f"{banks} Banks have been saved.")
    print("Starting to save state names into database.")
    states = save_states(state_set=state_set)
    print(f"{states} States have been saved.")
    print("Starting to save locations into database.")
    locations = save_locations(location_list=location_list)
    print(f"{locations} locations have been saved.")
    print("Starting to save branches into database.")
    branches = save_branches(data=data)
    print(f"{branches} branches have been saved.")


@transaction.atomic
def save_banks(bank_set):
    """
    This method will save all the banks in the database.
    :param bank_set:
    :return:
    """
    bank_obj = []
    for i in bank_set:
        bank_obj.append(Bank(name=i))
    Bank.objects.bulk_create(bank_obj)
    return len(bank_obj)


@transaction.atomic
def save_states(state_set):
    """
    This method will save all the states in the database.
    :param state_set:
    :return:
    """
    state_obj = []
    for i in state_set:
        state_obj.append(State(name=i))
    State.objects.bulk_create(state_obj)
    return len(state_obj)


@transaction.atomic
def save_locations(location_list):
    """
    This method will save all the locations in the database.
    :param location_list:
    :return:
    """
    j = 0
    for i in location_list:
        location, created = Location.objects.get_or_create(
            city=i['city'], district=i['district'], state=State.objects.get(name=i['state'])
        )
        if created:
            j += 1
        if j % 1000 == 0:
            print(f"\t{j} location objects have been processed.")
    return j


@transaction.atomic
def save_branches(data):
    """
    This method will save all the branches in the database.
    :param data:
    :return:
    """
    branches_obj = []
    j = 0
    for i in data:
        branches_obj.append(Branch(
            name=i['branch'],
            bank=Bank.objects.get(name=i['bank_name']),
            address=i['address'],
            ifsc_code=i['ifsc'],
            location=Location.objects.get(
                city=i['city'],
                district=i['district'],
                state=State.objects.get(name=i['state'])
            )
        ))
        j += 1
        if j % 5000 == 0:
            print(f"\t{j} branch objects have been processed.")
    Branch.objects.bulk_create(branches_obj)
    return len(branches_obj)
