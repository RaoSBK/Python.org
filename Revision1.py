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



# numbers = []
# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# print("Largest number:", max(numbers))

# print("Smallest number:", min(numbers))

# even_count = 0
# for n in numbers:
#     if n % 2 == 0:
#         even_count += 1

# print("Count of even numbers:", even_count)



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


# products = {}

# while True:
#     product_name = input("Enter product name (or type 'stop' to finish): ")
    
#     if product_name.lower() == "stop":
#         break
    
#     price = float(input(f"Enter price for {product_name}: "))
#     products[product_name] = price

# print("\nProducts entered:")
# for name, price in products.items():
#     print(f"{name}: {price}")

# total_cost = sum(products.values())
# print("\nTotal cost of all products:", total_cost)


#  Question 9 — String + Condition

# Write a program that:

# Takes a name as input
# Checks:
# If the name is in uppercase → print "Uppercase"
# If lowercase → print "Lowercase"
# Otherwise → print "Mixed case"


# Program to check case of a name

# # Take input
# name = input("Enter a name: ")

# if name == name.upper():
#     print("Uppercase")
# elif name == name.lower():
#     print("Lowercase")
# else:
#     print("Mixed case")



# Question 10 — While Loop + List + Removal

# Write a program that:

# Creates a list with duplicate values

# items = ["pen", "book", "pen", "pencil", "pen"]
# Removes all occurrences of "pen" using a while loop
# Prints the final list



items = ["pen", "book", "pen", "pencil", "pen"]

while "pen" in items:
    items.remove("pen")

print("Final list:", items)


# Question 11 — Number Analysis (Logic + Loop)

# Write a program that:

# Takes a number n from the user
# Prints all numbers from 1 to n
# Also:
# Count how many are even
# Count how many are odd


# n = int(input("Enter a number: "))

# even_count = 0
# odd_count = 0

# for i in range(1, n + 1):
#     print(i, end=" ") 
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("\nTotal even numbers:", even_count)
# print("Total odd numbers:", odd_count)




# Question 12 — Dictionary + Condition (Mini Filtering System)

# Write a program that:

# Has a dictionary of products and prices:
# products = {"pen": 10, "book": 50, "bag": 500, "pencil": 5}



# products = {"pen": 10, "book": 50, "bag": 500, "pencil": 5}

# limit = int(input("Enter a price limit: "))

# print(f"Products costing less than or equal to {limit}:")
# for item, price in products.items():
#     if price <= limit:
#         print(f"{item} - {price}")




# 🔹 Question 13 — Login System (While + Condition)

# Write a program that:

# Stores a correct username and password
# Asks the user to enter username and password
# Gives 3 attempts only
# If correct → print "Login Successful"
# If wrong after 3 attempts → print "Account Locked"


#Ans:
# correct_username = "admin"
# correct_password = "12345"

# attempts = 3

# while attempts > 0:
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if username == correct_username and password == correct_password:
#         print("Login Successful")
#         break
#     else:
#         attempts -= 1
#         print("Incorrect credentials. Attempts left:", attempts)

# if attempts == 0:
#     print("Account Locked")



# Question 14 — Shopping Cart (List + Input + Loop)

# Write a program that:

# Keeps asking the user to enter item names
# Stores items in a list
# Stops when user types "done"
# At the end:
# Print all items
# Print total number of items




# cart = []

# while True:
#     item = input("Enter item name (type 'done' to finish): ")

#     if item.lower() == "done":
#         break
#     else:
#         cart.append(item)

# print("\nItems in your cart:")
# for i in cart:
#     print("-", i)

# print("Total number of items:", len(cart))



# Question 15 — Number Guessing Game (While + Condition)

# Write a program that:

# Stores a secret number (e.g., 7)
# Asks the user to guess the number
# Keeps running until the user guesses correctly
# After each wrong guess:
# Print "Too high" or "Too low"





# secret_number = 7  
# guess = None      

# while guess != secret_number:
#     guess = int(input("Guess the number: "))  
    
#     if guess > secret_number:
#         print("Too high")
#     elif guess < secret_number:
#         print("Too low")

# print("Congratulations! You guessed it right.")




# Question 16 — Frequency Counter (List + Dictionary)

# Write a program that:

# Takes 5 numbers from the user
# Stores them in a list
# Creates a dictionary to count how many times each number appears

# 👉 Example:

# Input: 1 2 2 3 1  
# Output: {1: 2, 2: 2, 3: 1}





# numbers = []
# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# frequency = {}
# for num in numbers:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1

# print("Frequency count:", frequency)



# Question 17 — Palindrome Checker (String + Loop)

# Write a program that:

# Takes a word from the user
# Checks whether it is a palindrome (same forward and backward)
# Print:
# "Palindrome" or "Not Palindrome"


#Ans: 

# word = input("Enter a word: ")

# is_palindrome = True

# for i in range(len(word) // 2):
#     if word[i] != word[len(word) - 1 - i]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not Palindrome")




# Question 18 — Unique Elements (List + Logic)

# Write a program that:

# Takes 6 numbers from the user
# Stores them in a list
# Creates a new list containing only unique elements (no duplicates)
# Print the new list




# numbers = []  # list to store user input

# for i in range(6):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# unique_list = []  # list to store unique elements

# for n in numbers:
#     if n not in unique_list:
#         unique_list.append(n)

# print("Unique elements:", unique_list)




# Question 19 — Prime Number Check (Loop + Condition)

# Write a program that:

# Takes a number from the user
# Checks whether it is a prime number
# Print:
# "Prime" or "Not Prime"




# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not Prime")
# else:
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1): 
#         if num % i == 0:
#             is_prime = False
#             break
    
#     if is_prime:
#         print("Prime")
#     else:
#         print("Not Prime")



# Question 20 — Menu-Driven Program (While + Input + Condition)

# Write a program that:

# Shows a menu:

# 1. Add number  
# 2. Show list  
# 3. Exit  



# numbers = []  # list to store numbers

# while True:
#     print("\nMenu:")
#     print("1. Add number")
#     print("2. Show list")
#     print("3. Exit")

#     choice = input("Enter your choice (1-3): ")

#     if choice == "1":
#         num = int(input("Enter a number to add: "))
#         numbers.append(num)
#         print(f"{num} added to the list.")
#     elif choice == "2":
#         print("Current List:", numbers)
#     elif choice == "3":
#         print("Exiting program...")
#         break
#     else:
#         print("Invalid choice! Please enter 1, 2, or 3.")





# Question 21 — Password Strength Checker (String + Condition)

# Write a program that:

# Takes a password as input
# Checks:
# Length should be at least 6 characters
# Must contain at least one digit
# Print:
# "Strong Password" or "Weak Password"



password = input("Enter the password")

has_min_length = len(password) >=8
has_digit = any(char.isdigit() for char in password)

if has_min_length and has_digit:
    print("paassword is strong")
else:
    print("Password is not strong")


# Question 22 — Separate Even & Odd Numbers (List + Loop)

# Write a program that:

# Takes 6 numbers from the user
# Stores them in a list
# Creates two separate lists:
# One for even numbers
# One for odd numbers
# Print both lists

# 👉 Example:

# Input: 1 2 3 4 5 6  
# Output:
# Even: [2, 4, 6]  
# Odd: [1, 3, 5]



numbers = []

for i in range(6):
    num = int(input(f"Enter the number{i+1}"))
    numbers.append(num)


even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even: ",even)
print("Odd: ",odd)