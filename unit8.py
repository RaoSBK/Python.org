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

describe_pets(pet_name= 'harry', animal_type= 'Hmaster') # by usnign this method we are able to describe axjectly describes


