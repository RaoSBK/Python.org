# This one contains too many comments line cuse here I'm practicing about user input


# Q 6-12. Extensions: We’re now working with examples that are complex enough 
# that they can be extended in any number of ways. Use one of the example pro
# grams from this chapter, and extend it by adding new keys and values, chang
# ing the context of the program or improving the formatting of the output.

# Unit 7 : User Input and While Loops

# massage = input("Tell me somthing I'll repaeat it back: ")
# print(massage)

# name = input("Enter your full name")
# print(f"Your full name is: {name}")

prompt = "If you tell us who are you, we can personalize the massage for you see. "
prompt += "\n What is your first name"

# name= input(prompt)

# print(f"Hello {name}")


# Here we are trying to compare a string value with the int value so it is not possible thats why we got the error

# age = input("How old are you")
# age > 18
# print(f"age {age}")

# height = int(input("How tall are you, in inches"))
# if height >= 48:
#     print("\n You are tall enough to ride roller coster ")
# else:
#     print("\nYou'll be albe t ride when you're' a little older ")


# number = int(input("Enter number, and I'll tell you is it a even number or an odd number"))

# if number == 0:
#     print("your input is zero")
# elif number %2 == 0:
#     print("Given input is an even number")
# else:
#     print("Given number is an odd number ")

# Q 7-1. Rental Car: Write a program that asks the user what kind of rental car they 
# would like. Print a message about that car, such as “Let me see if I can find you 
# a Subaru.”

# car = input("What kind of rental car would you like?")

# print(f"Let me see if I can find you a {car}")


# Q 7-2. Restaurant Seating: Write a program that asks the user how many people 
# are in their dinner group. If the answer is more than eight, print a message say
# ing they’ll have to wait for a table. Otherwise, report that their table is ready

# ans:
# info = int(input("How many members are at the dinner"))

# if info > 8:
#     print("You'll have to wait for a table ")
# else:
#     print("Report that their table is reddy")


# Q 7-3. Multiples of Ten: Ask the user for a number, and then report whether the 
# number is a multiple of 10 or not.
#ans:
# number = int(input("Enter the number, and then I'll tell you is it a multiple of 10 or not "))

# if number % 10 == 0:
#     print("Given input is the multiple of 10")
# else:
#     print("Given input is not a multiple of 10")

# While loop is started 

# cureent_number = 1
# while cureent_number <=5:   #condition
#     print(cureent_number)
#     cureent_number += 1     # increment operator

# prompt = "\n Tell me something, and I'll  repeat it back"
# prompt += "Enter a 'quit' to end the program"

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     # print(message)

#     if message != 'quit':
#         print(message)


# #using flag

# prompt = "\n Tell me something, and I'll  repeat it back"
# prompt += "Enter a 'quit' to end the program"

# active = True
# message = ""
# while active:
#     message = input(prompt)
#     # print(message)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)


#using braek statement 

# prompt = "Enter the name of the city you have visited:  "
# prompt += "Enter a 'quit' to end the program "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to the {city.title()}")


# Using continue in the loop

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)


# x = 1
# while x <= 5:
#     print(x)
#     x +=1


# Q 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
# pizza toppings until they enter a 'quit' value. As they enter each topping, 
# print a message saying you’ll add that topping to their pizza.

# prompt = "Enter the pizza toppins"
# prompt += "\nEnter 'quit' when you want to exit"

# while prompt != 'quit':
#     message = input(prompt)
#     print(message)


# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on 
# a person’s age. If a person is under the age of 3, the ticket is free; if they are 
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is 
# $15. Write a loop in which you ask users their age, and then tell them the cost 
# of their movie ticket.

# while True:
#     age_input = input("Enter your age (or 'quit' to stop)")

#     if age_input.lower() == 'quit' :
#         print("Good bye")

#     try:
#         age = int(age_input)
#     except ValueError:
#         print("Please enter a valid age")
#         continue

#     if age < 3:
#         print("You ticket is free")

#     elif 3 <= age <= 12:
#         print("Your ticket cost is $10")
#     else:
#         print("your ticket cost is $15")



# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5 
# that do each of the following at least once:
# •	Use a conditional test in the while statement to stop the loop.
# •	Use an active variable to control how long the loop runs.
# •	Use a break statement to exit the loop when the user enters a 'quit' value.


#conditional statemnet

# age = ""
# while age != "quit":
#     age = input("Enter your age (or 'quit' to stop): ")
    
#     if age == "quit":
#         print("Goodbye!")
#     else:
#         age = int(age)
#         if age < 3:
#             print("Your ticket is free!")
#         elif 3 <= age <= 12:
#             print("Your ticket costs $10.")
#         else:
#             print("Your ticket costs $15.")


#with variable
# active = True

# while active:
#     age_input = input("Enter your age (or 'quit' to stop): ")
    
#     if age_input.lower() == "quit":
#         active = False
#     else:
#         age = int(age_input)
#         if age < 3:
#             print("Your ticket is free!")
#         elif 3 <= age <= 12:
#             print("Your ticket costs $10.")
#         else:
#             print("Your ticket costs $15.")

#using break statement

# while True:
#     age_input = input("Enter your age (or 'quit' to stop): ")
    
#     if age_input.lower() == "quit":
#         print("Goodbye!")
#         break
    
#     age = int(age_input)
#     if age < 3:
#         print("Your ticket is free!")
#     elif 3 <= age <= 12:
#         print("Your ticket costs $10.")
#     else:
#         print("Your ticket costs $15.")



# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press 
# ctrl-C or close the window displaying the output.

# while True:
#     print("This loop will run foreever!")           # this is the very danger code so after ruuning press 'ctrl+c'



# Moving item from one list to another

#starts with the user which needs to verify
# and an empty list to hold confirmed users

# unconfirmed_users = ['alice', 'bob', 'brain']
# confirmed_users= []

#verifying each users unitl they are they are no more unconfirmed users
# move each verified user into the list of confirmed users

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# # Display all conifermed users
# print("The following users are verified")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# Removing all instance of specific value from a list
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:        # we are able to remove or loop on the particular element of a list
#     pets.remove('cat')   

# print(pets)


# # Filling a dictionary with user input
# responses = {}

# # Set a flag to indicate that polling is active.
# polling_active = True

# while polling_active:
#     #Prompt for the person's name and response.
#     name = input("\n What is your name")
#     response = input("Whcih mountain would you like to climb someday?")

#     # Store the response in the dictionary
#     responses[name] = response

#     #Find out if anyone else is going to take the poll.
#     repeat = input("Would you like to let another person respond? (yes/ no)")
#     if repeat == 'no':
#         polling_active = False
#     # Polling is complete. Show the results.
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")



# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of vari
# ous sandwiches. Then make an empty list called finished_sandwiches. Loop 
# through the list of sandwich orders and print a message for each order, such 
# as I made your tuna sandwich. As each sandwich is made, move it to the list 
# of finished sandwiches. After all the sandwiches have been made, print a 
# message listing each sandwich that was made.


sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'veggie', 'pastrami', 'egg']
finished_sandwiches = []


while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    print(f"This sandwich is made {current_sandwiches}")

    finished_sandwiches.append(current_sandwiches)

print(finished_sandwiches)


# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure 
# the sandwich 'pastrami' appears in the list at least three times. Add code 
# near the beginning of your program to print a message saying the deli has 
# run out of pastrami, and then use a while loop to remove all occurrences of 
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up 


sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'veggie', 'pastrami', 'egg']

print("Sorry, the deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

finished_sandwiches = []

for order in sandwich_orders:
    print(f"I made your {order} sandwich.")
    finished_sandwiches.append(order)


print("\nSandwiches prepared:")
for sandwich in finished_sandwiches:
    print(sandwich)


# 7-10. Dream Vacation: Write a program that polls users about their dream vaca
# tion. Write a prompt similar to If you could visit one place in the world, where 
# would you go? Include a block of code that prints the results of the poll.



responses = {}  
polling_active = True

while polling_active:
    
    name = input("\nWhat is your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")

   
    responses[name] = vacation

    
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False


print("\n--- Dream Vacation Poll Results ---")
for name, vacation in responses.items():
    print(f"{name} would like to visit {vacation}.")