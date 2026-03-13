cars = ['audi','bmw', 'subaru',  'toyoto']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')


answer = 17
if answer != 43:
    print("That is not correct answer. Please try again")


age = 17

if age>=18:
    print("You're eligible to vote")
else:
    print("You're not eligible to vote")


age_1 = 15
age_2 = 25

if age_1 < 18 and age_2 >=18:
    print("The given input is correct input")

else:
    print("Given input is wrong input. try another input")


age_1 = 15
age_2 = 23

if age_1 < 18 or  age >= 18:
    print("Given input is right for only one person")
else:
    print("Try another input")


# checking the elements in the list
requested_toppings = ['mushrooms', 'onions', 'pineapples']
if 'mushroom' in requested_toppings :
    print("Available")
elif 'papperoine' in requested_toppings:
    print("Not availabe")

else :
    print("items are not available")


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish")

print("\n")

# Q 5-1. Conditional Tests: Write a series of conditional tests. Print a statement 
# describing each test and your prediction for the results of each test. Your code 
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# •	Look closely at your results, and make sure you understand why each line 
# evaluates to True or False.
# •	Create at least ten tests. Have at least five tests evaluate to True and 
# another five tests evaluate to False.

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("Is len(car) == 6? I predict True.")
print(len(car) == 6)

print("Is len(car) > 10? I predict False.")
print(len(car) > 10)

print("Is car.startswith('sub')? I predict True.")
print(car.startswith('sub'))

print("Is car.endswith('ru')? I predict True.")
print(car.endswith('ru'))

print("Is 'a' in car? I predict True.")
print('a' in car)

print("Is 'z' in car? I predict False.")
print('z' in car)


# Q 5-2. More Conditional Tests: You don’t have to limit the number of tests you 
# create to ten. If you want to try more comparisons, write more tests and add 
# them to conditional_tests.py. Have at least one True and one False result for 
# each of the following:
# •	Tests for equality and inequality with strings
# •	Tests using the lower() method
# •	Numerical tests involving equality and inequality, greater than and 
# less than, greater than or equal to, and less than or equal to
# •	Tests using the and keyword and the or keyword
# •	Test whether an item is in a list
# •	Test whether an item is not in a list

#String equality and inequality
car = 'Subaru'
print("Is car == 'Subaru'? I predict True")
print(car == 'Subaru')

print("Is car == 'subaru'? I predict False (case-sensetive)")
print(car == 'Subaru')

print("Is car != Audi? I predict True")
print(car != 'Subaru')

# using lower() method
print("Is lower() == 'subaru? I predict Trye.")
print(car.lower() == 'subaru')

print("Is car.lower() == 'subaru'? I predict False ")
print(car.lower() == 'Subaru')

#Numerical tests
age = 20
print("Is age == 20? I predict True:")
print(age == 20)

print("Is age !=30? I predict False")
print(age != 30)

print("Is age > 18? I predict True")
print(age > 18)

print("Is age is less than 18? I predict False")
print(age < 18)

print("Is age >= 20? I predict True")
print(age <= 20)

print("Is age >= 19? I predict True")
print(age<= 19)



# Membership tests with lists 
requested_toppings = ['mushrooms', 'onions', 'pineapples']
print("Is 'mushrooms' in requested_toppings? I  predic True")
print('mushrooms' in requested_toppings)

print("Is 'tiika' in requested_toopongs? I predict false")
print('tikka' in requested_toppings)