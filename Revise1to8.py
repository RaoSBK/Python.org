#  Unit 1
# Q1.

# Write a program that prints the following exactly:

# Hello Python!
# Welcome to Programming.


print("Hello Suraj")
print("Welcome to programming.")



# Chapter 2 – Variables & Simple Data Types
# Q3.

# Create variables for:

# Name
# Age
# City

# Print them using an f-string in one sentence.



Name = ("Suraj Bhan")
age = 18
City = ("Hyderabad")


print(f"My name is {Name.title()} , I am {age} years old and i am from {City} ")

# Q4.

# Take a string from the user and print:

# Uppercase version
# Lowercase version
# Title case version



# Name = input("Enter the an string: ")


print(Name.upper())
print(Name.lower())
print(Name.title())





# Chapter 3 – Introducing Lists
# Q5.

# Create a list of five favorite movies and:

# Print the first movie
# Print the last movie
# Print the total number of movies

fav_movies = ['interstellar', 'Oppenheimer', 'Tenet', 'Matrix', 'Shutter Island']

print(fav_movies[0])
print(fav_movies[-1])
print(len(fav_movies))



# Q6.

# Create a guest list with three names.

# Add one guest
# Remove one guest
# Print the final guest list


guests = ['Anderw', 'Sachin', 'martil']
guests.pop(1)
guests.insert(1,'suraj')


for guest in guests:
    print(guest)



# Chapter 4 – Working with Lists
# Q7.

# Generate numbers from 1 to 20 using range() and:

# Print the list
# Print the sum
# Print the maximum number

num = list(range(1,20))
print(num)
print(sum(num))
print(max(num))



# Q8.

# Create a list of squares from 1² to 10² using list comprehension.

# Example:

# [1,4,9,16,...]

Squares = [x**2 for  x in range(1, 11)]

print(Squares)





# Chapter 5 – if Statements
# Q9.

# Take a number from the user and print:

# Positive
# Negative
# Zero

# using if-elif-else.



# num = int(input("Enter the number: "))


# if(num == 0):
#     print("Given number is zero")
# elif(num > 0):
#     print("Given number is positive")
# else:
#     print("Given number is Negative")



# Q10.
# Take a username from the user.
# If username is "admin" print:

# Welcome Admin

# Otherwise print:

# Welcome User


# userName = input("Enter the User Name: ")

# if (userName == 'Admin'):
#     print("Welcome Admin")
# else:
#     print("Welcome User")





# Chapter 6 – Dictionaries
# Q11.

# Create a dictionary storing:

# name
# age
# branch

# Print all key-value pairs using .items().


student = {"Name": 'Suraj Bhan',
              'age': 18,
              'branch': 'Computer science and Enginerring '}

for key, value in student.items():
    print(key, ":", value)



# Q12.

# Create a dictionary of student marks and print only students who scored more than 75 marks.

# Example:

# {"Rahul":85,"Aman":60,"Riya":90}

marks = {"Rahul":85,
           "Aman":60,
           "Riya":90}

for name, score in marks.items():
    if score > 75:
        print(name, ":", score)




# Chapter 7 - User Input & While Loops
# Q13.

# Keep asking the user to enter a word.
# Stop only when user enters:

# quit

# Then display:

# Program Ended



# word = input("Enter a word")


# active = True
# message = ""

# while active:
#     message = input(word)

#     if message == 'quit':
#         active = False

#     else:
#         print(message)





# Q14.

# Take numbers continuously from the user until "stop" is entered.
# Print:

# Total count of numbers
# Sum of numbers



# num = []


# while True:
#     entry = input("Enter a number (or 'stop to finish): ")
#     if entry.lower() == "stop":
#         break
#     else:
#         num.append(int(entry))

# print("Total count of numbers: ", len(num))
# print("Sum of numbers: ", sum(num))




# Chapter 8 - Functions
# Q15.
# Create a function:
# def greet(name):
# that prints:
# Hello <name>
# Call it with at least three names.



def greet(name):
    print("Hello", name)

greet("Suraj")
greet("Rahul")
greet("Shivam")



# Q16.

# Create a function:

# def find_square(num):

# that returns the square of a number.

# Example:

# find_square(5)

# Output:

# 25


# num = int(input("Enter the number"))

# def find_square(num):
#     return num ** 2


# print(find_square(num))


# Write a function:

# def check_even_odd(num):

# The function should:

# Accept a number as a parameter
# Print "Even" if the number is even
# Print "Odd" if the number is odd



# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

check_even_odd(10)  
check_even_odd(7)  




# Question 18 — Maximum of Three Numbers

# Write a function:

# def find_max(a, b, c):

# The function should:

# Accept three numbers
# Return the largest number





def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Example usage
print(find_max(10, 25, 15))   
print(find_max(7, 3, 9))     
print(find_max(-5, -2, -8)) 





# Question 45 — Employee Attendance Tracker
# Write a function:
# def attendance_report(attendance):
# The function should:
# Accept a dictionary where:
# Key = Employee Name
# Value = Number of days present (out of 30)
# Calculate the attendance percentage for each employee.
# Print whether the employee is:
# Excellent (≥ 90%)
# Good (75%–89%)
# Needs Improvement (< 75%)


def attendance_report(attendance):
    for employee, days_present in attendance.items():
        # Calculate attendance percentage
        percentage = (days_present / 30) * 100

        # Determine category
        if percentage >= 90:
            status = "Excellent"
        elif 75 <= percentage < 90:
            status = "Good"
        else:
            status = "Needs Improvement"

        # Print report
        print(f"{employee}: {percentage:.2f}% - {status}")


attendance_data = {
    "Alice": 28,
    "Bob": 23,
    "Charlie": 30,
    "Diana": 20
}

attendance_report(attendance_data)





# Question 47 — Inventory Management System
# Write a function:
# def update_inventory(inventory, item, quantity):
# Requirements
# inventory is a dictionary where:
# Key = Item name
# Value = Quantity available
# If the item already exists, increase its quantity by the given amount.
# If the item does not exist, add it to the inventory with the given quantity.
# Return the updated inventory.





def update_inventory(inventory, item, quantity):
    """
    Updates the inventory dictionary with the given item and quantity.

    Parameters:
    inventory (dict): Current inventory with item names as keys and quantities as values.
    item (str): The item name to update or add.
    quantity (int): The quantity to add.

    Returns:
    dict: Updated inventory dictionary.
    """
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    return inventory



# Initial inventory
inventory = {"apple": 10, "banana": 5}

# Update existing item
print(update_inventory(inventory, "apple", 3))

# Add new item
print(update_inventory(inventory, "orange", 7))






# #classes

# Question 2 – Class with Attributes
# Create a class named Car.
# Add the following attributes:
# brand
# model
# year
# Create an object and print all the details.
# Example Output:
# Brand : Toyota
# Model : Fortuner
# Year : 2024


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def display_details(self):
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Year: ", self.year)


my_car = Car("BMW", "X5", 2024)


my_car.display_details()




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def display_detials(self):
        print("Name: ", self.name)
        print("salry: ", self.salary)



emp1 = Employee("john Doe", 50000)

emp1.display_detials()





# Question
# Create a class named Student that stores the student's name, roll number, and marks. Implement the following methods:
# accept_data() – Accept student details from the user.
# display_data() – Display the student's details.
# calculate_grade() – Calculate and display the grade based on the marks using the following criteria:
# Marks ≥ 90 → Grade A
# Marks ≥ 75 and < 90 → Grade B
# Marks ≥ 60 and < 75 → Grade C
# Marks ≥ 40 and < 60 → Grade D
# Marks < 40 → Grade F


# class Student:
#     def __init__(self):
#         self.name = ""
#         self.roll_number = ""
#         self.marks = 0

#     def accept_data(self):
#         self.name = input("Enter student name: ")
#         self.roll_number = input("Enter roll number: ")
#         self.marks = float(input("Enter marks: "))

#     def display_data(self):
#         print("\n--- Student Details ---")
#         print(f"Name: {self.name}")
#         print(f"Roll Number: {self.roll_number}")
#         print(f"Marks: {self.marks}")

#     def calculate_grade(self):
#         if self.marks >= 90:
#             grade = "A"
#         elif self.marks >= 75:
#             grade = "B"
#         elif self.marks >= 60:
#             grade = "C"
#         elif self.marks >= 40:
#             grade = "D"
#         else:
#             grade = "F"
#         print(f"Grade: {grade}")


# student1 = Student()
# student1.accept_data()
# student1.display_data()
# student1.calculate_grade()




# Question 12 — Car Class with Methods
# Create a class named Car.
# Requirements
# The class should have these attributes:
# brand
# model
# speed




class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, increment):
        """Increase the car's speed by a given amount."""
        self.speed += increment
        print(f"{self.brand} {self.model} accelerated to {self.speed} km/h.")

    def brake(self, decrement):
        """Decrease the car's speed by a given amount, not below 0."""
        self.speed = max(0, self.speed - decrement)
        print(f"{self.brand} {self.model} slowed down to {self.speed} km/h.")

    def honk(self):
        """Make the car honk."""
        print(f"{self.brand} {self.model} says: Beep Beep!")

    def display_info(self):
        """Show car details."""
        print(f"Car: {self.brand} {self.model}, Speed: {self.speed} km/h")



# Create a Car object
my_car = Car("Toyota", "Corolla")

# Display info
my_car.display_info()

# Accelerate and brake
my_car.accelerate(50)
my_car.brake(20)

# Honk
my_car.honk()






# Question 13 — Bank Account Class
# Create a class named:
# BankAccount
# Requirements
# The class should have these attributes:
# account_holder
# account_number
# balance



class BankAccount:
    def __init__(self, account_holder, account_number, balance=0.0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")



# Create an account
account1 = BankAccount("Suraj Bhan", "123456789", 5000)

# Perform operations
account1.display_info()
account1.deposit(1500)
account1.withdraw(2000)
account1.display_info()





# Question 14 — Employee Class with Salary Calculation

# Create a class named:

# Employee
# Requirements

# The class should have these attributes:

# name
# employee_id
# basic_salary


class Employee:
    def __init__(self, name, employee_id, basic_salary):
        self.name = name
        self.employee_id = employee_id
        self.basic_salary = basic_salary

    def calculate_salary(self):
        """
        Calculates total salary including allowances:
        - HRA = 40% of basic salary
        - DA = 20% of basic salary
        - Total Salary = Basic + HRA + DA
        """
        hra = 0.40 * self.basic_salary
        da = 0.20 * self.basic_salary
        total_salary = self.basic_salary + hra + da
        return total_salary

    def display_employee_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"Total Salary: {self.calculate_salary()}")


# Example usage
emp1 = Employee("Suraj Bhan", 101, 30000)
emp1.display_employee_details()





# Question 15 — ShoppingCart Class

# Create a class named:

# ShoppingCart
# Requirements

# The class should have:

# customer_name
# items — a list containing product names and prices




class ShoppingCart:
    def __init__(self, customer_name):
        # Initialize customer name and empty list of items
        self.customer_name = customer_name
        self.items = []  # Each item will be stored as a tuple (product_name, price)

    def add_item(self, product_name, price):
        # Add a product with its price to the cart
        self.items.append((product_name, price))

    def display_cart(self):
        # Show all items in the cart
        print(f"Shopping Cart for {self.customer_name}:")
        if not self.items:
            print("Your cart is empty.")
        else:
            for product, price in self.items:
                print(f"- {product}: ₹{price}")

    def calculate_total(self):
        # Calculate the total price of all items
        total = sum(price for _, price in self.items)
        return total


# Example usage
cart = ShoppingCart("Suraj")
cart.add_item("Laptop", 55000)
cart.add_item("Mouse", 1200)
cart.add_item("Keyboard", 2500)

cart.display_cart()
print("Total Bill: ₹", cart.calculate_total())
