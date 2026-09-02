# # Class

# class Student:


#     college_name= "Chaitanya deemed to be university"
#     #default constructors (constructor that create by default if you created or not that dont mind the python itself created it)
#     def __init__(self):   #The self parameter is a reference to the current instance of the class, and  is used to access variable that belongs to the class.
#         pass

#     # parameterized constructors
#     def __init__(self, fullname, marks):   #The self parameter is a reference to the current instance of the class, and  is used to access variable that belongs to the class.
#         self.name = fullname
#         self.marks = marks
#         print(self)
#         print("Adding the new student in the college database")

#     def welcome(self):
#         print("Welcome", self.name)

#     def get_marks(self):
#         return self.marks
    



# s1 = Student("Suraj Bhan", 97)
# print(s1.name, s1.marks, s1.college_name)
# s1.welcome()
# print(s1.get_marks())

# s2 = Student("Shivam", 87)
# print(s2.name, s2.marks)
# # print(s1.name)


# class Cars:
#     brand = "Range Rover"
#     price = "1 cr"


# c1 = Cars()
# print(c1.brand,"\n", c1.price)




# Q.No: 1
# Craete student class that takes name & marks of 3 subjects as argguments in constructor
#       Then create a method to print the average


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total =0
        for val in self.marks:
            total += val
        print("Hi ", self.name, "Your average marks is", total/3)

s1 = Student("Suraj Bhan", [90,95,80])
s1.get_avg()



#Making an instance from a class
class Dog:
    """A simple attempt to model a dog."""
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate the dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over")

    

my_dog = Dog('willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()



# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
# Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
# Make a method called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indi
# cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri
# butes individually, and then call both methods.

class Resturant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type

    def describe_restaurant(self):
        print(f"Restaurnat Name {self.restaurant_name}")
        print(f"Cusine Type {self.cusine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")


resturant = Resturant("21 Seven", "indian")


print(resturant.restaurant_name)
print(resturant.cusine_type)


resturant.describe_restaurant()
resturant.open_restaurant()




# Question 23 — Quiz Class

# Create a class named:

# Quiz

# The class should manage a simple multiple-choice quiz.

# Requirements

# The class should have:

# quiz_name
# questions — a list of questions
# score — initially 0


class Quiz:
    def __init__(self, quiz_name):
        self.quiz_name = quiz_name
        self.questions = []   # list of (question, options, correct_answer)
        self.score = 0

    def add_question(self, question, options, correct_answer):
        """Add a question with multiple-choice options."""
        self.questions.append({
            "question": question,
            "options": options,
            "answer": correct_answer
        })

    def take_quiz(self):
        """Run the quiz and calculate score."""
        print(f"\n--- {self.quiz_name} ---")
        for idx, q in enumerate(self.questions, start=1):
            print(f"\nQ{idx}: {q['question']}")
            for i, option in enumerate(q['options'], start=1):
                print(f"{i}. {option}")

            try:
                choice = int(input("Enter your choice (1-4): "))
                if q['options'][choice - 1] == q['answer']:
                    print("✅ Correct!")
                    self.score += 1
                else:
                    print(f"❌ Wrong! Correct answer: {q['answer']}")
            except (ValueError, IndexError):
                print("Invalid input! Skipping question.")

        print(f"\nYour final score: {self.score}/{len(self.questions)}")

# Example usage
quiz = Quiz("Python Basics Quiz")
quiz.add_question("What is the keyword to define a function in Python?",
                  ["func", "def", "function", "lambda"], "def")
quiz.add_question("Which data type is immutable?",
                  ["List", "Dictionary", "Tuple", "Set"], "Tuple")

quiz.take_quiz()






# Question 24 — ATM Class

# Create a class named:

# ATM

# The class should simulate a simple ATM machine.

# Requirements

# The class should have these attributes:

# account_holder
# balance
# pin



class ATM:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder
        self.balance = balance
        self.pin = pin

    def check_pin(self, entered_pin):
        return entered_pin == self.pin

    def deposit(self, amount, entered_pin):
        if self.check_pin(entered_pin):
            if amount > 0:
                self.balance += amount
                print(f"Deposited {amount}. New balance: {self.balance}")
            else:
                print("Deposit amount must be positive.")
        else:
            print("Invalid PIN!")

    def withdraw(self, amount, entered_pin):
        if self.check_pin(entered_pin):
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Invalid withdrawal amount or insufficient funds.")
        else:
            print("Invalid PIN!")

    def check_balance(self, entered_pin):
        if self.check_pin(entered_pin):
            print(f"Account Holder: {self.account_holder}")
            print(f"Current Balance: {self.balance}")
        else:
            print("Invalid PIN!")



# Create an ATM account
atm1 = ATM("Suraj Bhan", 5000, "1234")

# Correct PIN operations
atm1.check_balance("1234")
atm1.deposit(2000, "1234")
atm1.withdraw(1500, "1234")
atm1.check_balance("1234")

# Wrong PIN attempt
atm1.withdraw(500, "9999")
