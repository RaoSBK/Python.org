# Funcitons 

def greet_users():
    """Displaying a simple massage."""
    print("Hello")


greet_users()


def greet_users(user_name):
    """Displaying simple greet"""
    print(f"Hello {user_name.title()}")

greet_users('Suraj')


# 8-1. Message: Write a function called display_message() that prints one sen
# tence telling everyone what you are learning about in this chapter. Call the 
# function, and make sure the message displays correctly.

def display_message():
    """Displaying simple sentences"""
    print("What you are learning about in this chapter")

display_message()



# 8-2. Favorite Book: Write a function called favorite_book() that accepts one 
# parameter, title. The function should print a message, such as One of my 
# favorite books is Alice in Wonderland. Call the function, making sure to 
# include a book title as an argument in the function call.

def favorite_book(book):
    """Passing Argument in the funciton"""
    print(f"One of my favorite books in {book.title()} in Wonderla")

favorite_book('alice')



# passing Argumment 
# Positional Arguments

def describe_pets(animal_type, pet_name):
    """Display information about pets"""
    print(f"I have a {animal_type.title()}")
    print(f'My {animal_type.title()} name is {pet_name.title()}')

describe_pets('Hamster', 'harry')

# multiple calling
describe_pets('dog', 'whillie')

# keywrods argument 
describe_pets(pet_name= 'harry', animal_type= 'Hmaster') # by usnign this method we are able to describe axjectly describes

describe_pets(pet_name= 'commb', animal_type= 'squarel')

# Default values

def describing_pets(pet_name, animal_type='Dog'):
    """Describing pets"""
    print(f"I have a {animal_type.title()}")
    print(f"My {animal_type} name is {pet_name}")

describing_pets(pet_name= 'willee')



# Q 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the 
# text of a message that should be printed on the shirt. The function should print 
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the 
# function a second time using keyword arguments.



#-----ANS---

# def make_shirt(size, message):
#     size = input("Enter the size of the T-Shirt")
#     message = input("Enter the message which you want to print on the T-Shirt")

#     print(f"------The size of the T-Shirt is {size}, and this T-Shirt printing is started-----")
#     print(f"{message}")
#     print(f"--------------T-Shirt is printed----------------------------")

# make_shirt(size= input, message= input)


# Q 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large 
# by default with a message that reads I love Python. Make a large shirt and a 
# medium shirt with the default message, and a shirt of any size with a different 
# message.


# ----ANS----

# def make_shirts(message, size = 'Large'):
#     message= input("Enter the message which you want to print on the T-Shirts: ")
#     print(f"-------T-Shirt size is {size} and it's Printing is Started-------")
#     print(message)
#     print("-----------T-Shirt is printed----------")

# make_shirts(message= input)



# Q 8-5. Cities: Write a function called describe_city() that accepts the name of 
# a city and its country. The function should print a simple sentence, such as 
# Reykjavik is in Iceland. Give the parameter for the country a default value. 
# Call your function for three different cities, at least one of which is not in the 
# default country.


def describe_city(city, country = 'india'):
    print(f"{city.title()} is in  {country.title()}")

describe_city('Hyderabad')
describe_city('Mumbai')
describe_city('Reykjavik', country= 'iceland')



#Returning simple value
def get_formated_name(first_name, last_name):
    """Return a full name neatly formated"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formated_name('Suraj', 'Bhan')
print(musician)


def get_formated_name(first_name, middle_name, last_name):
    """Return a full name neatly formated"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formated_name('suraj', 'bhan', 'kumar')
print(musician)

# User dont have middle name every time then this above funciton is not working then we need to follow another way

def get_name_formated(first_name, last_name, middle_name=''):
    """Return full name, neatly formated"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician =  get_name_formated('jimi', 'hendrix')
print(musician)

musician = get_name_formated('jhon', 'hooker', 'lee')
print(musician)


# Return a Dictionary
def build_person(first_name, last_name):
    """Return a dictionary of infromation about a person"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimmi', 'hindrix')
print(musician)


# Return a Dictionary with the optional value
def build_person(first_name, last_name, age= None):
    """Return a dictionary of information about a perosn"""
    person = {'frist': first_name, 'last': last_name}
    if age:
        person['age']= age
    return person

musician = build_person('jimmi', 'hendrix', age=35)
print(musician)