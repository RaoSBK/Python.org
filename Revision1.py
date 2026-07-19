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



# password = input("Enter the password")

# has_min_length = len(password) >=8
# has_digit = any(char.isdigit() for char in password)

# if has_min_length and has_digit:
#     print("paassword is strong")
# else:
#     print("Password is not strong")


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



# numbers = []

# for i in range(6):
#     num = int(input(f"Enter the number{i+1}"))
#     numbers.append(num)


# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even: ",even)
# print("Odd: ",odd)



# Question 23 — Sum of Digits (Loop + Logic)

# Write a program that:

# Takes a number from the user
# Calculates the sum of its digits



# Program to calculate sum of digits

# num = int(input("Enter a number: "))

# digit_sum = 0

# while num > 0:
#     digit = num % 10      
#     digit_sum += digit   
#     num = num // 10      

# # Step 4: Print result
# print("Sum of digits =", digit_sum)



# Question 24 — Reverse a List (List + Loop)

# Write a program that:

# Takes 5 elements from the user into a list
# Creates a new list with elements in reverse order (without using .reverse())
# Print the reversed list




# my_list = []
# for i in range(5):
#     element = input(f"Enter element {i+1}: ")
#     my_list.append(element)

# reversed_list = []
# for i in range(len(my_list)-1, -1, -1):   # loop backwards
#     reversed_list.append(my_list[i])

# print("Original list:", my_list)
# print("Reversed list:", reversed_list)



# Question 25 — Count Vowels (String + Loop)

# Write a program that:

# Takes a sentence from the user
# Counts how many vowels (a, e, i, o, u) are present
# Print the total count



# sentence = input("Enter a sentence: ")

# vowel_count = 0

# vowels = "aeiouAEIOU"

# for char in sentence:
#     if char in vowels:
#         vowel_count += 1

# print("Total number of vowels:", vowel_count)



# Question 26 — Find Second Largest Number (List + Logic)

# Write a program that:

# Takes 5 numbers from the user
# Finds the second largest number in the list
# Print it




# numbers = []
# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# numbers.sort(reverse=True)

# second_largest = numbers[1]

# print("The second largest number is:", second_largest)



# Question 27 — Factorial of a Number (Loop + Logic)

# Write a program that:

# Takes a number from the user
# Calculates its factorial




# num = int(input("Enter a number: "))

# factorial = 1

# for i in range(1, num + 1):
#     factorial *= i

# print("Factorial of", num, "is:", factorial)



# Question 28 — Common Elements in Two Lists (List + Condition)

# Write a program that:

# Takes two lists of numbers from the user
# Finds and prints the common elements between them



# list1 = list(map(int, input("Enter numbers for List 1 (space-separated): ").split()))
# list2 = list(map(int, input("Enter numbers for List 2 (space-separated): ").split()))

# common_elements = []
# for num in list1:
#     if num in list2 and num not in common_elements:
#         common_elements.append(num)

# if common_elements:
#     print("Common elements:", common_elements)
# else:
#     print("No common elements found.")




# Question 29 — Remove Duplicates (List + Logic)

# Write a program that:

# Takes a list of numbers from the user
# Removes all duplicate values
# Prints a list with only unique elements (without using set())




# user_input = input("Enter values (space-separated): ").split()

# numbers = []
# for item in user_input:
#     if item.isdigit():   
#         numbers.append(int(item))
#     else:
#         print(f"Skipping invalid input: {item}")

# unique_numbers = []
# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)

# print("List with unique elements:", unique_numbers)



# Question 30 — Simple Calculator (Menu + Loop)

# Write a program that:

# Displays a menu:

# 1. Add  
# 2. Subtract  
# 3. Multiply  
# 4. Divide  
# 5. Exit  
# Takes user choice and two numbers
# Performs the selected operation
# Runs continuously until user chooses Exit



# while True:
#     print("\n--- Simple Calculator ---")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == '5':
#         print("Exiting calculator. Goodbye!")
#         break

#     try:
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))
#     except ValueError:
#         print("Invalid input! Please enter numeric values.")
#         continue

#     if choice == '1':
#         print("Result:", num1 + num2)
#     elif choice == '2':
#         print("Result:", num1 - num2)
#     elif choice == '3':
#         print("Result:", num1 * num2)
#     elif choice == '4':
#         if num2 != 0:
#             print("Result:", num1 / num2)
#         else:
#             print("Error: Division by zero is not allowed.")
#     else:
#         print("Invalid choice! Please select from 1 to 5.")



# Question 31 — Armstrong Number Check (Loop + Logic)

# Write a program that:

# Takes a number from the user
# Checks whether it is an Armstrong number




# num = int(input("Enter a number: "))

# num_str = str(num)
# num_digits = len(num_str)

# armstrong_sum = 0

# for digit in num_str:
#     armstrong_sum += int(digit) ** num_digits

# if armstrong_sum == num:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is NOT an Armstrong number")



# Question 32 — Count Words in Sentence (String + Loop)

# Write a program that:

# Takes a sentence from the user
# Counts how many words are present
# Print total words



# sentence = input("Enter a sentence: ")

# word_count = 0

# in_word = False

# for char in sentence:
#     if char != " " and not in_word:
#         in_word = True
#         word_count += 1
#     elif char == " ":
#         in_word = False

# print("Total number of words:", word_count)



# Question 33 — Fibonacci Series (Loop + Logic)

# Write a program that:

# Takes a number n from the user
# Prints the first n terms of the Fibonacci series



# n = int(input("Enter the number of terms: "))

# a, b = 0, 1

# print("Fibonacci Series:")

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b



# Question 34 — Count Characters (String + Dictionary)

# Write a program that:

# Takes a string from the user
# Counts how many times each character appears
# Store result in a dictionary



# text = input("Enter a string: ")

# char_count = {}

# for char in text:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1

# print("Character frequencies:", char_count)





# Question 35 — Anagram Checker (String + Logic)

# Write a program that:

# Takes two strings from the user
# Checks whether they are anagrams (same characters, different order)
# Ignore spaces and case



# def is_anagram(str1, str2):
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
    
#     return sorted(str1) == sorted(str2)

# string1 = input("Enter first string: ")
# string2 = input("Enter second string: ")

# if is_anagram(string1, string2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")


# Question 36 — Running Average (While + Input + Aggregation)

# Write a program that:

# Continuously asks the user to enter numbers
# Stops when the user types "stop"
# Calculates and prints the average of entered numbers



# total = 0
# count = 0

# while True:
#     user_input = input("Enter a number (or type 'stop' to finish): ")

#     if user_input.lower() == "stop":
#         break

#     try:
#         number = float(user_input)
#         total += number
#         count += 1
#     except ValueError:
#         print("Invalid input! Please enter a number or 'stop'.")

# if count > 0:
#     average = total / count
#     print("Average of entered numbers:", average)
# else:
#     print("No numbers were entered.")



# Question 37 — Number Pattern (Loop + Nested Logic)

# Write a program that:

# Takes a number n from the user
# Prints the following pattern:



# n = int(input("Enter the number of rows: "))

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()  # Move to next line


# Question 38 — Highest Frequency Element (List + Dictionary)

# Write a program that:

# Takes a list of numbers from the user
# Finds the element that appears most frequently
# Prints that element



# numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# frequency = {}

# for num in numbers:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1

# max_freq = max(frequency.values())
# for key, value in frequency.items():
#     if value == max_freq:
#         print("Element with highest frequency:", key)
#         break


# Question 39 — Reverse a Number (Loop + Math Logic)

# Write a program that:

# Takes a number from the user
# Reverses the number
# Prints the reversed number

# num = int (input("Enter a number:"))

# reversed_num = 0
# temp = num


# while temp > 0:
#     digit = temp % 10
#     reversed_num = reversed_num * 10 + digit
#     temp //= 10

#     print("Reversed number =  ", reversed_num)


# Question 40 — Student Grade System (Dictionary + Condition)

# Write a program that:

# Stores student names and marks in a dictionary
# Prints grades based on marks:



# students = {
#     "Alice": 85,
#     "Bob": 72,
#     "Charlie": 90,
#     "David": 60,
#     "Eva": 45
# }

# def get_grade(marks):
#     if marks >= 90:
#         return "A+"
#     elif marks >= 80:
#         return "A"
#     elif marks >= 70:
#         return "B"
#     elif marks >= 60:
#         return "C"
#     elif marks >= 50:
#         return "D"
#     else:
#         return "F"

# for name, marks in students.items():
#     print(name, ":", get_grade(marks))


# Question 41 — Find Missing Number (List + Logic)

# Write a program that:

# Takes a list containing numbers from 1 to n
# One number is missing
# Find and print the missing number



# n = int(input("Enter the value of n: "))
# numbers = list(map(int, input("Enter the numbers separated by space: ").split()))

# expected_sum = n * (n + 1) // 2

# actual_sum = sum(numbers)

# missing_number = expected_sum - actual_sum

# print("The missing number is:", missing_number)





# Question 42 — Simple Voting System (While + Dictionary)

# Write a program that:

# Allows users to vote for a candidate
# Store votes in a dictionary
# Continue voting until user types "stop"
# At the end:
# Print total votes for each candidate
# Print winner (highest votes)



# n = int(input("Enter the value of n: "))
# numbers = list(map(int, input("Enter the numbers separated by space: ").split()))

# expected_sum = n * (n + 1) // 2

# actual_sum = sum(numbers)

# missing_number = expected_sum - actual_sum

# print("The missing number is:", missing_number)



# Question 43 — Matrix Addition (Nested Lists + Loops)

# Write a program that:

# Takes two 2x2 matrices from the user
# Adds them element by element
# Prints the resulting matrix



# print("Enter elements of first 2x2 matrix:")
# matrix1 = []
# for i in range(2):
#     row = []
#     for j in range(2):
#         val = int(input(f"Enter element [{i+1}][{j+1}]: "))
#         row.append(val)
#     matrix1.append(row)

# print("\nEnter elements of second 2x2 matrix:")
# matrix2 = []
# for i in range(2):
#     row = []
#     for j in range(2):
#         val = int(input(f"Enter element [{i+1}][{j+1}]: "))
#         row.append(val)
#     matrix2.append(row)

# result = []
# for i in range(2):
#     row = []
#     for j in range(2):
#         row.append(matrix1[i][j] + matrix2[i][j])
#     result.append(row)

# print("\nResultant Matrix after Addition:")
# for row in result:
#     print(row)




# Question 44 — Longest Word Finder (String + List Logic)

# Write a program that:

# Takes a sentence from the user
# Finds the longest word in the sentence
# Prints the word and its length



# sentence = input("Enter a sentence: ")

# words = sentence.split()

# longest_word = ""
# max_length = 0

# for word in words:
#     if len(word) > max_length:
#         longest_word = word
#         max_length = len(word)

# print("Longest word:", longest_word)
# print("Length:", max_length)



# Question 45 — Remove Spaces from String (String Processing)

# Write a program that:

# Takes a sentence from the user
# Removes all spaces from the string
# Prints the updated string



# sentence = input("Enter a sentence: ")

# updated_sentence = sentence.replace(" ", "")

# print("String without spaces:", updated_sentence)



# Question 46 — Merge Two Dictionaries (Dictionary + Loop)

# Write a program that:

# Creates two dictionaries
# Merges them into a single dictionary
# If same key exists, add their values together



# dict1 = {"a": 10, "b": 20, "c": 30}
# dict2 = {"b": 5, "c": 15, "d": 25}

# merged_dict = dict1.copy()  
# for key, value in dict2.items():
#     if key in merged_dict:
#         merged_dict[key] += value  
#     else:
#         merged_dict[key] = value  

# print("Merged Dictionary:", merged_dict)



# Question 47 — Perfect Number Check (Loop + Math Logic)

# Write a program that:

# Takes a number from the user
# Checks whether it is a Perfect Number




# num = int(input("Enter a number: "))

# sum_of_divisors = 0

# for i in range(1, num):
#     if num % i == 0:  
#         sum_of_divisors += i

# if sum_of_divisors == num:
#     print(num, "is a Perfect Number")
# else:
#     print(num, "is NOT a Perfect Number")


# Question 48 — Rotate a List (List Manipulation)

# Write a program that:

# Takes a list and a number k from the user
# Rotates the list to the right by k positions



# numbers = list(map(int, input("Enter the list elements separated by space: ").split()))
# k = int(input("Enter the value of k: "))

# k = k % len(numbers)

# rotated_list = numbers[-k:] + numbers[:-k]

# print("Rotated List:", rotated_list)



# Question 49 — Check Balanced Parentheses (Stack Logic using List)

# Write a program that:

# Takes an expression from the user
# Checks whether parentheses are balanced




# def is_balanced(expression):
#     stack = []
#     pairs = {')': '(', '[': ']', '}': '{'}
    
#     for char in expression:
#         if char in "([{":
#             stack.append(char)
#         elif char in ")]}":
#             if not stack or stack[-1] != pairs[char]:
#                 return False
#             stack.pop()

#     return len(stack) == 0

# expr = input("Enter an expression: ")

# if  is_balanced(expr):
#     print("Parentheses are balanced.")
# else:
#     print("Parantheses are NOT balanced.")



# Question 50 — Find Duplicate Elements (List + Frequency Logic)

# Write a program that:

# Takes a list of numbers from the user
# Finds all duplicate elements
# Prints duplicates only once


# number = list(map(int, input("Enter numbers separated by space:").split()))

# frequency = {}

# for num in numbers:
#     if num in frequency:
#         frequency[num] +=1
#     else:
#         frequency[num] = 1

# duplicates = []
# for key, value in frequency.items():
#     if value > 1:
#         duplicates.append(key)

# if duplicates:
#     print("Duplicate elements: ", duplicates)
# else:
#     print("No duplicates found.")



# Question 51 — Decimal to Binary Converter (Loop + Math Logic)

# Write a program that:

# Takes a decimal number from the user
# Converts it into binary format without using bin()

# Program: Decimal to Binary Converter

# num = int(input("Enter a decimal number: "))

# binary = ""
# temp = num

# while temp > 0:
#     remainder = temp % 2          
#     binary = str(remainder) + binary  
#     temp //= 2                


# print("Binary representation of", num, "is:", binary)




# Question 52 — Find Pair with Given Sum (List + Nested Loop)

# Write a program that:

# Takes a list of numbers and a target sum
# Finds all pairs whose sum equals the target



# numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# target = int(input("Enter the target sum: "))

# print("Pairs with sum", target, ":")
# found = False
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print(numbers[i], "+", numbers[j], "=", target)
#             found = True

# if not found:
#     print("No pairs found.")




# Question 53 — Check Leap Year (Condition + Logic)

# Write a program that:

# Takes a year from the user
# Checks whether it is a Leap Year



# year = int(input("Enter a year: "))

# if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
#     print(year, "is a Leap Year")
# else:
#     print(year, "is NOT a Leap Year")



# Question 54 — Sort List Without Using sort() (Logic Building)

# Write a program that:

# Takes a list of numbers from the user
# Sorts the list in ascending order without using sort() or sorted()



# numbers = list(map(int, input("Enter numbers (space-separated): ").split()))


# for i in range(len(numbers)):
#     for j in range(len(numbers) - i - 1):
#         if numbers[j] > numbers[j + 1]:
#             # Swap elements
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# print("Sorted list in ascending order:", numbers)



# Question 55 — Find All Divisors of a Number (Loop + Math Logic)

# Write a program that:

# Takes a number from the user
# Prints all its divisors



# num = int(input("Enter a number: "))

# print("Divisors of", num, "are:")

# for i in range(1, num + 1):
#     if num % i == 0: 
#         print(i)




# Question 56 — Simple Contact Book (Dictionary + Loop)

# Write a program that:

# Creates a contact book using a dictionary
# Menu options:



# contacts = {} 

# while True:
#     print("\n--- Contact Book Menu ---")
#     print("1. Add Contact")
#     print("2. View Contact")
#     print("3. Delete Contact")
#     print("4. Show All Contacts")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == '1':
#         name = input("Enter contact name: ")
#         number = input("Enter contact number: ")
#         contacts[name] = number
#         print("Contact added successfully!")

#     elif choice == '2':
#         name = input("Enter contact name to view: ")
#         if name in contacts:
#             print("Name:", name, " | Number:", contacts[name])
#         else:
#             print("Contact not found!")

#     elif choice == '3':
#         name = input("Enter contact name to delete: ")
#         if name in contacts:
#             del contacts[name]
#             print("Contact deleted successfully!")
#         else:
#             print("Contact not found!")

#     elif choice == '4':
#         if contacts:
#             print("\n--- All Contacts ---")
#             for name, number in contacts.items():
#                 print("Name:", name, " | Number:", number)
#         else:
#             print("No contacts available.")

#     elif choice == '5':
#         print("Exiting Contact Book. Goodbye!")
#         break

#     else:
#         print("Invalid choice! Please select from 1 to 5.")





# Question 57 — Check Whether Two Lists Are Equal (List + Logic)

# Write a program that:

# Takes two lists from the user
# Checks whether both lists are equal
# Print:
# "Equal" if same elements in same order
# "Not Equal" otherwise




# list1 = list(map(int, input("Enter numbers for List 1 (space-separated): ").split()))
# list2 = list(map(int, input("Enter numbers for List 2 (space-separated): ").split()))


# if list1 == list2:
#     print("Equal")
# else:
#     print("Not Equal")





# Question 58 — Count Uppercase, Lowercase, and Digits (String Processing)

# Write a program that:

# Takes a string from the user
# Counts:
# Uppercase letters
# Lowercase letters
# Digits



# text = input("Enter a string: ")

# uppercase_count = 0
# lowercase_count = 0
# digit_count = 0

# for char in text:
#     if char.isupper():
#         uppercase_count += 1
#     elif char.islower():
#         lowercase_count += 1
#     elif char.isdigit():
#         digit_count += 1

# # Print results
# print("Uppercase letters:", uppercase_count)
# print("Lowercase letters:", lowercase_count)
# print("Digits:", digit_count)



# uestion 59 — Find GCD of Two Numbers (Math + Loop Logic)

# Write a program that:

# Takes two numbers from the user
# Finds their Greatest Common Divisor (GCD) without using built-in functions


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# gcd = 1

# for i in range(1, min(num1, num2) + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i  

# print("GCD of", num1, "and", num2, "is:", gcd)




# Question 60 — Word Frequency Counter (String + Dictionary)

# Write a program that:

# Takes a sentence from the user
# Counts how many times each word appears
# Store result in a dictionary



# sentence = input("Enter a sentence: ")

# words = sentence.split()

# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1

# print("Word frequencies:", word_count)





# Question 61 — Check Whether a Number is Palindrome (Math + Loop)

# Write a program that:

# Takes a number from the user
# Reverses the number
# Checks whether the original number and reversed number are same




# num = int(input("Enter a number: "))

# original_num = num

# reversed_num = 0

# while num > 0:
#     digit = num % 10            
#     reversed_num = reversed_num * 10 + digit  
#     num //= 10                    


# if original_num == reversed_num:
#     print(original_num, "is a Palindrome number")
# else:
#     print(original_num, "is NOT a Palindrome number")






# list1 = list(map(int, input("Enter numbers for List 1 (space-separated): ").split()))
# list2 = list(map(int, input("Enter numbers for List 2 (space-separated): ").split()))

# intersection = []

# for num in list1:
#     if num in list2 and num not in intersection:
#         intersection.append(num)

# if intersection:
#     print("Intersection of lists:", intersection)
# else:
#     print("No common elements found.")




# Question 63 — Find LCM of Two Numbers (Math + Logic)

# Write a program that:

# Takes two numbers from the user
# Finds their Least Common Multiple (LCM) without using built-in functions




# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# greater = num1 if num1 > num2 else num2

# while True:
#     if greater % num1 == 0 and greater % num2 == 0:
#         lcm = greater
#         break
#     greater += 1

# print("Lcm of", num1, "and", num2, "is", lcm)



# number = list(map(int, input("Enter numbers (space-separated): ").split()))


# is_sorted = True


# for  i in range(len(numbers) -1):
#     if numbers[i] > numbers[i+1]:
#         is_sorted = False
#         break

# if is_sorted:
#     print("The list is sorted in ascending order.")
# else:
#     print("The list is NOT sorted in ascending order.")






# text = input("Enter a string: ")

# char_count = {}

# for char in text:
#     char_count[char] = char_count.get(char, 0) + 1

# first_non_repeating = None
# for char in text:
#     if char_count[char] == 1:
#         first_non_repeating = char
#         break

# if first_non_repeating:
#     print("First non-repeating character:", first_non_repeating)
# else:
#     print("No non-repeating character found.")








# Question 66 — Move All Zeros to End (List Manipulation)

# Write a program that:

# Takes a list of numbers from the user
# Moves all 0s to the end of the list
# Keep the order of non-zero elements same





# numbers = list(map(int, input("Enter numbers (space-separated): ").split()))

# result = [num for num in numbers if num != 0]

# zero_count = numbers.count(0)

# result.extend([0] * zero_count)

# print("List after moving zeros to the end:", result)




# Write a function:

# def factorial(n):

# The function should:

# Accept a number as a parameter
# Calculate its factorial
# Return the result


def factorial(n):
    """
    Calculate the factorial of a number n.
    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result



print(factorial(5))




# Question 21 — Student Grade Function

# Write a function:

# def calculate_grade(marks):

# The function should:

# Accept marks as a parameter
# Return the grade according to:




def calculate_grade(marks):
    """
    Return grade based on marks.
    :param marks: Integer (0–100)
    :return: Grade as string
    """
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"
    

print(calculate_grade(95))  
print(calculate_grade(82)) 
print(calculate_grade(67))
print(calculate_grade(45)) 




# Question 22 — Reverse a String Using a Function
# Write a function:
# def reverse_string(text):
# The function should:
# Accept a string as a parameter
# Return the reversed string



# def reverse_string(text):
#     return text[::-1]


# word = input("Enter a word: ")
# print("Reverse string is:", reverse_string(word))




# Question 23 — Count Even Numbers in a List
# Write a function:
# def count_even(numbers):
# The function should:
# Accept a list of numbers
# Count how many numbers are even
# Return the count


def count_even(numbers):
    count = 0
    for number in numbers:
        if number %2 ==0:
            count += 1
    return count

nums = [1, 2, 3, 4, 5, 6, 7, 8]
print("Count even numbers", count_even(nums))


# Question 24 — Create a Username Function
# Write a function:
# def create_username(first_name, last_name):
# The function should:
# Accept first name and last name
# Create a username by joining them with an underscore (_)
# Convert the username to lowercase
# Return the username


def create_username(first_name, last_name):
    username = first_name + "_" + last_name
    return username.lower()

# Example usage
print(create_username("Suraj", "Kumar"))  
print(create_username("Alice", "Smith"))   
print(create_username("John", "Doe"))      





# Question 25 — Sum of List Elements Function
# Write a function:
# def calculate_sum(numbers):
# The function should:
# Accept a list of numbers
# Calculate the sum of all elements
# Return the sum



def calculate_sum(numbers):
    return sum(numbers)

print(calculate_sum([1, 2, 3, 4, 5])) 
print(calculate_sum([10, -2, 8]))       
print(calculate_sum([]))              




# Question 26 — Find the Smallest Number Function
# Write a function:
# def find_smallest(numbers):
# The function should:
# Accept a list of numbers
# Find the smallest number
# Return the smallest number

def find_smallest(numbers):
    return min(numbers)


nums = [12, 5, 20, 4]
print("The smallest number in the list is", find_smallest(nums))


# Question 27 — Palindrome Function
# Write a function:
# def is_palindrome(text):
# The function should:
# Accept a string
# Return True if the string is a palindrome
# Return False otherwise


def is_palindrome(text):
    cleaned = text.replace("","").lower()
    return cleaned == cleaned[::-1]


print(is_palindrome("madam"))      
print(is_palindrome("racecar"))     
print(is_palindrome("hello"))      
print(is_palindrome("A man a plan a canal Panama"))




# Question 28 — Count Words Function
# Write a function:
# def count_words(sentence):
# The function should:
# Accept a sentence as a parameter
# Count the total number of words
# Return the count



def count_words(sentence):
    # Split the sentence into words using spaces
    words = sentence.split()
    # Return the total number of words
    return len(words)


print(count_words("Programming is fun"))      
print(count_words("Hello world from Python"))



# Question 29 — Find Common Elements Function
# Write a function:
# def common_elements(list1, list2):
# The function should:
# Accept two lists
# Find common elements
# Return them in a new list




def common_elements(list1, list2):
    result = []
    for item in list1:
        if item in list2 and item not in result:
            result.append(item)
    return result

# Example usage
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))  
print(common_elements(["apple", "banana"], ["banana", "cherry"])) 




# Question 30 — Student Result Function
# Write a function:
# def student_result(marks):
# The function should:
# Accept a list of marks
# Calculate the average marks
# Return:
# "Pass" if average ≥ 40
# "Fail" otherwise



def student_result(marks):
    if not marks:
        return "No marks provided"
    
    average = sum(marks)/ len(marks)

    if average >= 40:
        return "Pass"
    else:
        return "fail"
    
print(student_result([50, 60, 70]))
print(student_result([10,10,10]))
print(student_result([90, 80, 40]))



# Question 31 — Frequency Counter Function
# Write a function:
# def frequency_count(items):
# The function should:
# Accept a list
# Count how many times each element appears
# Return a dictionary



def frequency_count(items):
    freq = {}

    for item in items:
        if item in freq:
            freq[item] +=1
        else:
            freq[item] = 1
        
    return freq


print(frequency_count([1, 2, 2, 3, 1, 4, 2]))
print(frequency_count(["apple", "banana", "apple", "orange", "banana"]))




# Question 32 — Find Second Largest Number Function
# Write a function:
# def second_largest(numbers):
# The function should:
# Accept a list of numbers
# Find the second largest number
# Return it


def second_largest(numbers):
    unique_numbers = list(set(numbers))
    
    if len(unique_numbers) < 2:
        return None
    
    unique_numbers.sort(reverse=True)
    
    return unique_numbers[1]

nums = [12, 45, 7, 30, 45]
print("Second largest number:", second_largest(nums))




# Question 33 — Remove Duplicates Function
# Write a function:
# def remove_duplicates(items):
# The function should:
# Accept a list
# Remove duplicate elements
# Return a new list containing only unique elements



def remove_duplicates(items):
    unique_items = []
    
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    
    return unique_items

data = [4, 2, 7, 4, 9, 2, 4, 7]
print("List without duplicates:", remove_duplicates(data))



# Question 32 — Find Second Largest Number Function
# Write a function:
# def second_largest(numbers):
# The function should:
# Accept a list of numbers
# Find the second largest number
# Return it



def second_largest(numbers):
    unique_numbers = list(set(numbers))
    
    # Check if there are at least 2 unique numbers
    if len(unique_numbers) < 2:
        return None  # No second largest exists
    
    # Sort in descending order
    unique_numbers.sort(reverse=True)
    
    # Return the second largest
    return unique_numbers[1]


nums = [12, 45, 7, 30, 45]
print("Second largest number is:", second_largest(nums))


# Question 33 — Remove Duplicates Function
# Write a function:
# def remove_duplicates(items):
# The function should:
# Accept a list
# Remove duplicate elements
# Return a new list containing only unique elements



def remove_duplicates(items):
    # Create a new list to store unique elements
    unique_items = []
    
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    
    return unique_items


# Example usage:
data = [4, 2, 7, 4, 9, 2, 4, 7]
print("List without duplicates:", remove_duplicates(data))



# Question 34 — Merge Two Sorted Lists Function
# Write a function:
# def merge_sorted_lists(list1, list2):
# The function should:
# Accept two already sorted lists
# Merge them into a single sorted list
# Return the new list



def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print("Merged Sorted List:", merge_sorted_lists(list1, list2))






# Question 35 — Password Validator Function
# Write a function:
# def validate_password(password):
# The function should return True only if:
# Password length is at least 8 characters
# Contains at least one digit
# Contains at least one uppercase letter
# Otherwise return False.




def validate_password(password):
    if len(password) < 8:
        return False
    
    has_digit = any(char.isdigit() for char in password)
    
    has_upper = any(char.isupper() for char in password)
    
    return has_digit and has_upper


print(validate_password("Pass1234"))   
print(validate_password("password"))  
print(validate_password("PASSWORD1")) 
print(validate_password("Pass12"))   



# Question 36 — Most Frequent Element Function
# Write a function:
# def most_frequent(numbers):
# The function should:
# Accept a list of numbers
# Find the element that appears the most times
# Return that element


# Function to find the most frequent element in a list
def most_frequent(numbers):
    frequency = {}
    
    # Count occurrences
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Find element with maximum frequency
    max_freq = max(frequency.values())
    for key, value in frequency.items():
        if value == max_freq:
            return key

# Example usage
print(most_frequent([4, 2, 7, 4, 9, 2, 4, 7]))   # Output: 4
print(most_frequent([1, 1, 2, 2, 3, 3]))         # Output: 1 (first max found)




# Question 37 — Count Vowels and Consonants Function
# Write a function:
# def count_vowels_consonants(text):
# The function should:
# Accept a string
# Count vowels and consonants separately
# Return both counts



# Function to count vowels and consonants in a string
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    # Loop through each character
    for char in text:
        if char.isalpha():  # Only consider letters
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

# Example usage
v, c = count_vowels_consonants("Programming is fun")
print("Vowels:", v)        # Output: 5
print("Consonants:", c)    # Output: 10




# Question 36 — Most Frequent Element Function
# Write a function:
# def most_frequent(numbers):
# The function should:
# Accept a list of numbers
# Find the element that appears the most times
# Return that element



# Function to find the most frequent element in a list
def most_frequent(numbers):
    frequency = {}
    
    # Count occurrences
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Find element with maximum frequency
    max_freq = max(frequency.values())
    for key, value in frequency.items():
        if value == max_freq:
            return key

# Example usage
print(most_frequent([4, 2, 7, 4, 9, 2, 4, 7]))   # Output: 4
print(most_frequent([1, 1, 2, 2, 3, 3]))         # Output: 1 (first max found)






# Question 37 — Count Vowels and Consonants Function
# Write a function:
# def count_vowels_consonants(text):
# The function should:
# Accept a string
# Count vowels and consonants separately
# Return both counts


# Function to count vowels and consonants in a string
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    # Loop through each character
    for char in text:
        if char.isalpha():  # Only consider letters
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

# Example usage
v, c = count_vowels_consonants("Programming is fun")
print("Vowels:", v)        # Output: 5
print("Consonants:", c)    # Output: 10





# Question 38 — Shopping Cart Total Function
# Write a function:
# def calculate_total(prices):
# The function should:
# Accept a list of item prices
# Calculate the total bill
# Return the total amount


def calculate_total(prices):
    return sum(prices)

print(calculate_total([100, 250, 75]))   # Output: 425
print(calculate_total([49.99, 19.99, 5])) # Output: 74.98
print(calculate_total([]))               # Output: 0




# Question 39 — Find Longest Word Function
# Write a function:
# def longest_word(words):
# The function should:
# Accept a list of words
# Find the longest word
# Return that word



def longest_word(words):
    # Handle empty list case
    if not words:
        return None
    
    # Initialize longest word
    longest = words[0]
    
    # Loop through words to find the longest
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Example usage
print(longest_word(["apple", "banana", "cherry", "watermelon"]))  # Output: watermelon
print(longest_word(["hi", "hello", "hey"]))                       # Output: hello
print(longest_word([]))                                           # Output: None




# Question 40 — Employee Salary Calculator
# Write a function:
# def calculate_salary(hours_worked, hourly_rate):
# The function should:
# Accept the number of hours worked and hourly rate.
# If an employee works more than 40 hours, every extra hour should be paid at 1.5× the hourly rate.
# Return the total salary.


def calcualte_salary(hours_worked, hourly_rate):
    if hours_worked < 40:
        salary = hours_worked * hourly_rate
        return salary
    else:
        regular_salary = hourly_rate * 40
        overTime_hours = hours_worked - 40
        overTime_salary = overTime_hours * (hourly_rate * 1.5)
        salary = regular_salary + overTime_salary
        return salary
    


print(calcualte_salary(35, 70))
print(calcualte_salary(45, 70))




# Question 41 — Student Report Card
# Write a function:
# def student_report(name, marks):
# The function should:
# Accept a student's name and a list of marks.
# Calculate:
# Total marks
# Average marks
# Return a dictionary containing:
# Student name
# Total
# Average
# Grade
# Grade Criteria
# Average	Grade
# 90+	A
# 75–89	B
# 60–74	C
# 40–59	D
# Below 40	Fail



def student_report(name, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 40:
        grade = "D"
    else:
        grade = "Fail"
    return {
        "Name": name,
        "Total Marks": total,
        "Average Marks": average,
        "Grade": grade,
    }


print(student_report("Suraj Bhan", [68,70,90]))



# Problem 42 — Library Book Management System

# Write a program using functions that manages a small library.



library = []  

# Function to add a book
def add_book(book_id, title, author):
    book = {"ID": book_id, "Title": title, "Author": author, "Available": True}
    library.append(book)
    print(f"Book '{title}' added successfully!")

# Function to display all books
def display_books():
    if not library:
        print("No books in the library.")
    else:
        print("\n--- Library Books ---")
        for book in library:
            status = "Available" if book["Available"] else "Issued"
            print(f"ID: {book['ID']} | Title: {book['Title']} | Author: {book['Author']} | Status: {status}")

# Function to issue a book
def issue_book(book_id):
    for book in library:
        if book["ID"] == book_id:
            if book["Available"]:
                book["Available"] = False
                print(f"Book '{book['Title']}' issued successfully!")
            else:
                print("Sorry, this book is already issued.")
            return
    print("Book not found!")

# Function to return a book
def return_book(book_id):
    for book in library:
        if book["ID"] == book_id:
            if not book["Available"]:
                book["Available"] = True
                print(f"Book '{book['Title']}' returned successfully!")
            else:
                print("This book was not issued.")
            return
    print("Book not found!")

# Function to search for a book
def search_book(title):
    found = False
    for book in library:
        if book["Title"].lower() == title.lower():
            status = "Available" if book["Available"] else "Issued"
            print(f"Found: ID: {book['ID']} | Title: {book['Title']} | Author: {book['Author']} | Status: {status}")
            found = True
    if not found:
        print("Book not found!")

def menu():
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            add_book(book_id, title, author)
        elif choice == "2":
            display_books()
        elif choice == "3":
            book_id = input("Enter Book ID to issue: ")
            issue_book(book_id)
        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            return_book(book_id)
        elif choice == "5":
            title = input("Enter Book Title to search: ")
            search_book(title)
        elif choice == "6":
            print("Exiting Library System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
