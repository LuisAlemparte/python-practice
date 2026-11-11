# PCC chapter 6 exercises

# 6-7 People: a list of person-dicts, loop and print each one.
person_1 = {'first_name': 'luis', 'last_name': 'alemparte', 'age': 23, 'city': 'karlsruhe'}
person_2 = {'first_name': 'jacob', 'last_name': 'amao', 'age': 25, 'city': 'london'}
person_3 = {'first_name': 'enrico', 'last_name': 'fermi', 'age': 53, 'city': 'chicago'}
people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}".title()
    print(f"{full_name}, {person['age']}, lives in {person['city'].title()}.")

print()

# 6-8 Pets: a list of dicts, each {'kind': ..., 'owner': ...}.
#     Make 3 pets, put them in a list `pets`, loop and print "<Owner> has a <kind>."
pet_1 = {'kind': 'dog', 'owner': 'luis'}
pet_2 = {'kind': 'cat', 'owner': 'jacob'}
pet_3 = {'kind': 'parrot', 'owner': 'enrico'}
pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"{pet['owner'].title()} has a {pet['kind']}.")

print()


# 6-9 Favorite places: a dict name -> list of 1-3 places.
#     Make `favorite_places` for 3 people, loop and print each person's places, one per line.
favorite_places = {
    'luis': ['madrid', 'granada', 'karlsruhe'],
    'jacob': ['london'],
    'enrico': ['rome', 'chicago'],
}

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places:")
    for place in places:
        print(f"  {place.title()}")

