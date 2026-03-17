# Dictnary

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])



alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points")


alien_0 = {'color': 'green', 'points': 5}

alien_0['X position'] = 0
alien_0['Y position'] = 25
print(alien_0)

alien_0 = {'color': 'green',}
print(f"The aliean is {alien_0['color']}")

alien_0['color'] = 'Yellow'
print(f"The alian is {alien_0['color']}")

alien_0 = {'X position': 0, 'Y position': 25, 'speed': 'Medium'}

if alien_0['speed'] ==  'slow':
    x_increment = 1
elif alien_0['speed'] ==  'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['X position'] = alien_0['X position'] + x_increment

print(f"New position: {alien_0['X position']}")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


fav_lang = {'jen': 'python', 'edward': 'java', 'sarah': 'c', 'phil': 'python'}
lang = fav_lang['sarah'].title()
print(f"Sarah favourite langauge is {lang}.")


# alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned ')
print(point_value)


# Q 6-1. Person: Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. You 
# should have keys such as first_name, last_name, age, and city. Print each 
# piece of information stored in your dictionary.

person = {'first_Name': 'Suraj_Bhan', 'last_name': 'Kumar', 'age': '18', 'City': 'Hyderabad',}


print(person)

# Q 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
# Think of five names, and use them as keys in your dictionary. Think of a favorite 
# number for each person, and store each as a value in your dictionary. Print 
# each person’s name and their favorite number. For even more fun, poll a few 
# friends and get some actual data for your program.


fav_number = {'Rahul': '1', 'Ratan': '2', 'Utsav': '3', 'Suraj': '4', 'Shivam': '5'}

print(fav_number)


# Q 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. 
# However, to avoid confusion, let’s call it a glossary.
# •	Think of five programming words you’ve learned about in the previous 
# chapters. Use these words as the keys in your glossary, and store their 
# meanings as values.
# •	Print each word and its meaning as neatly formatted output. You might 
# print the word followed by a colon and then its meaning, or print the word 
# on one line and then print its meaning indented on a second line. Use the 
# newline character (\n) to insert a blank line between each word-meaning 
# pair in your output

glossary = {'list': 'muttable collections of elemets ', 'tupple': 'immutable collection of elements'}


value = glossary.get('list', 'No point value assigned')

print(value)
value = glossary.get('tupple', 'No point value assigned')

print(value)

user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}

for key, value in user_0.items():
    print(f"\n Key: {key}")
    print(f"\n Value: {value}")

print("\n")

fav_langs = {'jan': 'python', 'sarah': 'c', 'edward': 'ruby', 'pjil': 'python'}

for name, lang in fav_langs.items():
    print(f"{name.title()}'s favourite language is {lang.title()}. ")

friends  = ['phil', 'sarah']
for name in fav_langs.keys():
    print(name.title())

    if name in friends:
        langs = fav_langs[name].title()
        print(f"\t {name.title()}, I see you loved {langs}")


fav_langs =  {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python'}
if 'erin' not in fav_langs.keys():
    print('Erin, please take out pool')


fav_langs =  {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python'}
for name in sorted(fav_langs.keys()):
    print(f'{name.title()}, thank you for polling.')


fav_langs =  {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python'}
print("The following languages are mentioned ")
for lang in fav_langs.values():
    print(lang.title())


fav_langs =  {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python'}
print("The following langs are mentioned ")
for langs in set(fav_langs.values()):
    print(langs.title())



# Q  6-4. Glossary 2: Now that you know how to loop through a dictionary, clean 
# up the code from Exercise 6-3 (page 99) by replacing your series of print() 
# calls with a loop that runs through the dictionary’s keys and values. When 
# you’re sure that your loop works, add five more Python terms to your glossary. 
# When you run your program again, these new words and meanings should 
# automatically be included in the output.  

glossaries = {'list': 'muttable collections of elemets ', 'tupple': 'immutable collection of elements'}

for key, glossary in glossaries.items():
    print(f"{key.title()}, i learned in the previous unit ")


# Q 6-5. Rivers: Make a dictionary containing three major rivers and the country 
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# •	Use a loop to print a sentence about each river, such as The Nile runs 
# through Egypt.
# •	Use a loop to print the name of each river included in the dictionary.
# •	Use a loop to print the name of each country included in the dictionary.

rivers = {'nile': 'egypt','amazon': 'brazil','yangtze': 'china'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers included in the dictionary:")
for river in rivers.keys():
    print(river.title())

print("\nCountries included in the dictionary:")
for country in rivers.values():
    print(country.title())


rivers = {'nile': 'egypt', 'amazon': 'brazil', 'yangtze': 'china'}

for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(river)


for country in rivers.values():
    print(country.title())


# Q 6-6. Polling: Use the code in favorite_languages.py (page 97).
# •	Make a list of people who should take the favorite languages poll. Include 
# some names that are already in the dictionary and some that are not. 
# •	Loop through the list of people who should take the poll. If they have 
# already taken the poll, print a message thanking them for responding. 
# If they have not yet taken the poll, print a message inviting them to take 
# the poll

# favorite_languages.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'mike', 'anna', 'david']

for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, please take the poll and share your favorite language.")



# Nesting

alien_0 = {'color': 'green', 'point': 5}
alien_1 = {'color': 'yellow', 'point': 10}
alien_2 = {'color': 'red', 'point': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("\n")
# creating a range of aliens 

aliens= []
for alien_number in range(30):
    new_alien= {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien ['color'] == 'green':
        alien ['color'] = 'yellow'
        alien ['speed'] = 'medium'
        alien['points'] = 10

    elif alien ['color'] == 'yellow':
        alien ['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'


for alien in aliens[:5]:
    print(alien)
print("...")

print(f"Total number of aliens is : {len(aliens)}")

# creating list in the dictionay

pizza = {
    'crust': 'thick',
    'toppings': ['moshrooms', 'extra cheese']
}

print(f"You required a {pizza['crust']} crust pizza " "with the followings toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)



favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages  in favorite_languages.items():
    print(f"\n {name.title()}, favourite languages are: ")
    for language in languages:
        print(f"\t {language.title()}")


# you can create many dictionary in one dictionary

users = {
    'suraj01': {'first_name': 'Suraj', 'last_name': 'Bhan', 'location': 'Hyderabad'},
    'Shiavam01': {'first_name': 'Shivam', 'last_name': 'Chaurasiya', 'location': 'Hyderabad'},
    'Goutam01': {'first_name': 'Goutam', 'last_name': 'bahi', 'location': 'Hyderabaad'},
}

for username, user_info in users.items():
    print(f"\n User Name {username}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info['location']


    print(f"Full Name: {full_name}")
    print(f"Location {location}")


users = {
    'suraj01': {'first_name': 'Suraj', 'last_name': 'Bhan', 'location': 'Hyderabad'},
    'Shiavam01': {'first_name': 'Shivam', 'last_name': 'Chaurasiya', 'location': 'Hyderabad'},
    'Goutam01': {'first_name': 'Goutam', 'last_name': 'bahi', 'location': 'Hyderabaad'},
}

for username, user_info in users.items():
    print(f"User Name: {username}")

    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    locations = user_info['location']

    print(f"\t User Name {full_name}")
    print(f'\t Location {locations}')


# Q 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). 
# Make two new dictionaries representing different people, and store all three 
# dictionaries in a list called people. Loop through your list of people. As you 
# loop through the list, print everything you know about each person.


person1 = {'first_Name': 'Suraj_Bhan', 'last_name': 'Kumar', 'age': '18', 'City': 'Hyderabad',},
person2 = {'first_Name': 'Shivam', 'last_name': 'Chaurasiya', 'age': '18', 'City': 'Hyderabad',},
person3 = {'first_Name': 'Goutam', 'last_name': 'gambhir', 'age': '18', 'City': 'Hyderabad',}

people = [person1, person2, person3]

for person in people:
    print(person)


# Q 6-8. Pets: Make several dictionaries, where each dictionary represents a differ
# ent pet. In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list and as 
# you do, print everything you know about each pet.

pet1 = {"animal": "dog", "owner": "Alice"}
pet2 = {"animal": "cat", "owner": "Bob"}
pet3 = {"animal": "parrot", "owner": "Charlie"}
pet4 = {"animal": "rabbit", "owner": "Diana"}


pets = [pet1, pet2, pet3, pet4]
for pet in pets:
    print(f"Pet name: {pet['animal']}")
    print(f"Owner: {pet['owner']}")


# Q 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three 
# names to use as keys in the dictionary, and store one to three favorite places 
# for each person. To make this exercise a bit more interesting, ask some friends 
# to name a few of their favorite places. Loop through the dictionary, and print 
# each person’s name and their favorite places.

favorite_places = {
    "Alice": ["Paris", "New York", "Tokyo"],
    "Bob": ["London", "Rome"],
    "Charlie": ["Sydney", "San Francisco", "Berlin"]
}

for name, places in favorite_places.items():
    print(f"{name} favourite places are: ")
    for place in places:
        print(f" {place}")


# Q 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) 
# so each person can have more than one favorite number. Then print each per
# son’s name along with their favorite numbers.

favorite_numbers = {
    "Alice": [3, 7, 21],
    "Bob": [5, 10],
    "Charlie": [2, 4, 6, 8]
}

for name, numbers in favorite_numbers.items():
    print(f"{name} favourite numbers are: ")
    for number in numbers:
        print(f" {number}")


# Q6-11. Cities: Make a dictionary called cities. Use the names of three cities as 
# keys in your dictionary. Create a dictionary of information about each city and 
# include the country that the city is in, its approximate population, and one fact 
# about that city. The keys for each city’s dictionary should be something like 
# country, population, and fact. Print the name of each city and all of the infor
# mation you have stored about it.


cities = {
    "Paris": {
        "country": "France",
        "population": "2.1 million",
        "fact": "Known as the City of Light and famous for the Eiffel Tower."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "13.9 million",
        "fact": "Home to the busiest train station in the world, Shinjuku."
    },
    "New York": {
        "country": "USA",
        "population": "8.6 million",
        "fact": "Famous for Times Square and being a global financial hub."
    }
}

for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {country}")
    print(f"population: {info['population']}")
    print(f"fact: {info['fact']}")