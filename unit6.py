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