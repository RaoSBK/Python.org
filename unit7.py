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

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


x = 1
while x <= 5:
    print(x)
    x +=1


# Q 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of 
# pizza toppings until they enter a 'quit' value. As they enter each topping, 
# print a message saying you’ll add that topping to their pizza.

prompt = "Enter the pizza toppins"
prompt += "\nEnter 'quit' when you want to exit"

while prompt != 'quit':
    message = input(prompt)
    print(message)