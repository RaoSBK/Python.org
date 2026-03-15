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

value = glossary.get('\n''tupple', 'No point value assigned')

print(value)


