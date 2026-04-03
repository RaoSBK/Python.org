# Question 1 — Basics + Conditions

# Write a Python program that:

# Takes a number from the user
# Checks whether the number is:
# Positive, Negative, or Zero
# Also check whether it is even or odd



# x = int(input("Enter the number"))

# if x > 0:
#     print("Given nuber is positive")
#     if x % 2 == 0:
#         print("Given number is even")
#     else:
#         print("Given number is odd")
# elif x < 0:
#     print("Given number is negative ")
#     if x % 2 == 0:
#         print("Given number is even")
#     else:
#         print("Given number is odd")
# else:
#     print("Given number is zero")


# Question 2 — Lists + Loop + Condition

# Create a program that:

# Stores 5 favorite fruits in a list
# Loops through the list

fav_fruits = ['Guava', 'banana', 'apple', 'grapes', 'mango']

for fruit in fav_fruits:
    print(f"I like {fruit}")



# Question 3 — While Loop + Dictionary (Important)

# Write a program that:

# Asks users for their name and favorite programming language
# Stores responses in a dictionary
# Keeps asking until user enters "no"
# At the end, prints all responses

responses = {}

# while True:
#     name = input("Enter your name or say (no) to stop: ")

#     if name.lower() == "no":
#         break

#     language = input ("Enter your faavorite programming language: ")
#     responses[name] = language

# print("\n All Responses ")

# for person, lang in responses.items():
#     print(f"{person} likes {lang}")


# Question 4 — List + While + Condition

# Write a program that:

# Creates a list of numbers from 1 to 10
# Uses a while loop to:
# Print only odd numbers
# Skip even numbers using continue

# 👉 Concepts covered:

# while loop
# % operator



numbers = list(range(1, 11))

i = 0

while i < len(numbers):
    if numbers[i] % 2 == 0:
        i += 1
        continue  
    
    print(numbers[i])
    
    i += 1


# Question 5 — Dictionary + Loop + Condition

# Create a dictionary of 5 students with their marks:

# students = {"A": 85, "B": 45, "C": 72, "D": 30, "E": 90}

# Write a program that:

# Loops through the dictionary
# Prints:
# "Pass" if marks ≥ 50
# "Fail" if marks < 50


students = {"A": 85, "B": 45, "C": 72, "D": 30, "E": 90}

for name, marks in students.items():
    if marks >= 50:
        print(name, "Pass")
    else:
        print(name, "Fail")


# Question 6 — User Input + While Loop (Logic Building)

# Write a program that:

# Asks the user to enter numbers continuously
# Stops when the user enters "stop"
# At the end, prints:
# Total numbers entered
# Sum of numbers


# count = 0
# total_sum = 0

# while True:
#     user_input = input("Enter a number (or type 'stop' to end): ")
    
#     if user_input.lower() == "stop":
#         break 
    
#     number = int(user_input)
    
#     count += 1
#     total_sum += number

# print("Total numbers entered:", count)
# print("Sum of numbers:", total_sum)



# uestion 7 — Lists + Condition + Loop (Real Logic)

# Write a program that:

# Takes 5 numbers from the user and stores them in a list
# After storing:
# Print the largest number
# Print the smallest number
# Print how many numbers are even



numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print("Largest number:", max(numbers))

print("Smallest number:", min(numbers))

even_count = 0
for n in numbers:
    if n % 2 == 0:
        even_count += 1

print("Count of even numbers:", even_count)



# Question 8 — Dictionary + While Loop + Input (Mini System)

# Write a program that:

# Creates an empty dictionary
# Asks user to enter:
# Product name
# Price
# Store them in dictionary
# Continue asking until user types "stop"
# At the end:
# Print all products
# Print total cost of all products


products = {}

while True:
    product_name = input("Enter product name (or type 'stop' to finish): ")
    
    if product_name.lower() == "stop":
        break
    
    price = float(input(f"Enter price for {product_name}: "))
    products[product_name] = price

print("\nProducts entered:")
for name, price in products.items():
    print(f"{name}: {price}")

total_cost = sum(products.values())
print("\nTotal cost of all products:", total_cost)
