def greet_user(username):
    print(f"Hello, {username.title()}!")

greet_user('jesse')

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(animal_type='dog',pet_name='willie')

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last':last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


# --- Exercises (your code) ---

# 8-1 Message: display_message() prints one sentence about what you're learning in this chapter. Call it.
def display_messege():
    print("This chapter is about functions")
display_messege()

# 8-3 T-Shirt: make_shirt(size, text) prints the size and the text.
#     Call it once with positional arguments, once with keyword arguments.
def make_shirt(shirt_size, shirt_text):
    print(f"\nShirt size is {shirt_size}.")
    print(f"\nShirt text is {shirt_text}.")
    make_shirt("L", "Hello World")
    make_shirt(shirt_text="Hello World", shirt_size="M")



# 8-6 City Names: city_country(city, country) RETURNS "Santiago, Chile". Call it 3 times, print the results.
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

print(city_country("santiago", "chile"))

def make_album(artist, title, tracks=None):
    album = {"artist": artist.title(), "title": title.title()}
    if tracks:
        album["tracks"] = tracks
    return album

print(make_album("star", "girl"))
print(make_album("drake", "scorpion"))
print(make_album("adele", "25", tracks=11))