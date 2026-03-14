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


age = 19
if age >18:
    print("You can vote")
    print("Have you registed to vote yet?")
else: 
    print("You're not elgible to vote")
    print("Please register to vote as soon as you turn 18.")



age = 20
if age < 5:
    print("You are in less than 4  yrs old so your addmision fee is free")
elif age > 5 and age < 18:
    print("Your addmision fee is $25")
elif age >= 18:
    print("Your addmison fee is $40")
else:
    print("You enterd wrong value")


age = 12
if age <  4:
    price = 0
elif age >4 and age < 18:
    price = 25
elif age > 18:
    price = 40

print(f"Your admmions cost is ${price}.")


requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'papperoini' in requested_toppings:
    print("Adding papperoini")
if 'extra cheese' in requested_toppings:
    print("adding extra cheese")



print("\n Finished making pizza")



requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
elif 'papperoini' in requested_toppings:
    print("Adding papperoini")
elif 'extra cheese' in requested_toppings:
    print("adding extra cheese")

print("\n Finished making pizza")



# Q 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a 
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# •	Write an if statement to test whether the alien’s color is green. If it is, print 
# a message that the player just earned 5 points.
# •	Write one version of this program that passes the if test and another that 
# fails. (The version that fails will have no output.)


alien_color = 'green'
if alien_color == 'green':
    print("You got 5 points")



# Q 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and 
# write an if-else chain.
# •	If the alien’s color is green, print a statement that the player just earned 
# 5 points for shooting the alien.
# •	If the alien’s color isn’t green, print a statement that the player just earned 
# 10 points.
# •	Write one version of this program that runs the if block and another that 
# runs the else block.

alien_color = 'green'

if alien_color == 'green':
    print("You secured 5 points")
elif alien_color  == 'red':
    print('You loss 5 points')
else:
    print('You secured 10 points')

# Q 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif
# else chain.
# •	If the alien is green, print a message that the player earned 5 points.
# •	If the alien is yellow, print a message that the player earned 10 points.
# •	If the alien is red, print a message that the player earned 15 points.
# •	Write three versions of this program, making sure each message is printed 
# for the appropriate color alien.


alien_color = 'green'

if alien_color == 'green':
    print("You secured 5 points")
elif alien_color  == 'yellow':
    print('You secured 10 points')
elif alien_color == 'red':
    print("You secured 15 points")
else:
    print('You secured 10 points')


print("Is alian color is green? I assumed true")
print(alien_color == 'green')

print("Is alian color is red? I assuned false ")
print(alien_color == 'red')


# Q 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s 
# stage of life. Set a value for the variable age, and then:
# •	If the person is less than 2 years old, print a message that the person is 
# a baby.
# •	If the person is at least 2 years old but less than 4, print a message that 
# the person is a toddler.
# •	If the person is at least 4 years old but less than 13, print a message that 
# the person is a kid.
# •	If the person is at least 13 years old but less than 20, print a message that 
# the person is a teenager.
# •	If the person is at least 20 years old but less than 65, print a message that 
# the person is an adult.
# •	If the person is age 65 or older, print a message that the person is an 
# elder.

age = 45

if age < 2:
    print("you are a baby")
elif age > 2 and age < 4:
    print("you are a toddler")
elif age >= 4 and age < 13:
    print("You are a kid")
elif age >= 13 and age < 20:
    print("You are a teenager")
elif age >= 20 and age < 65:
    print("Your are an adult")
elif age >= 65:
    print("Your are an elder person")
else:
    print("You enterd an wrong age")



# Q 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of 
# independent if statements that check for certain fruits in your list.
# •	Make a list of your three favorite fruits and call it favorite_fruits.
# •	Write five if statements. Each should check whether a certain kind of fruit 
# is in your list. If the fruit is in your list, the if block should print a statement, 
# such as You really like bananas!

fav_fruits = ['banana', 'guava', 'mango']
if 'banana' in fav_fruits:
    print("You really like banana")
if 'guava' in fav_fruits:
    print("You really like guava")
if 'mango' in fav_fruits:
    print("You really like mango")
else:
    print("Fruits is not available")


requested_toppings =  ['mushrooms', 'green papers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")

print("\n Finished making pizza")


requested_toppings =  ['mushrooms', 'green pappers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green pappers':
        print("Sorry green papper is out of stock right now")
    else:
        print(f"Adding {requested_topping}")

print("\n Finished making pizza")


requested_toppings =  []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("Finished making your pizza")
else:
    print("Are you sure You want a plain pizza")

print("\n")

available_toppings =  ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'green pappers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry we don't have {requested_topping}")

print("Finished Your making pizza")

# Q 5-8. Hello Admin: Make a list of five or more usernames, including the name 
# 'admin'. Imagine you are writing code that will print a greeting to each user 
# after they log in to a website. Loop through the list, and print a greeting to 
# each user:
# •	If the username is 'admin', print a special greeting, such as Hello admin, 
# would you like to see a status report?
# •	Otherwise, print a generic greeting, such as Hello Jaden, thank you for 
# logging in again.

users = ['admin', 'michel', 'sophea', 'simen', 'elon' ]

for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report")
    else:
        print(f"Hello {user}, thank you for logging in again")

    

# Q 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is 
# not empty.
# •	If the list is empty, print the message We need to find some users!
# •	Remove all of the usernames from your list, and make sure the correct 
# message is printed


users = []

if not users:
    print("We need to find new users")
else:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report")
        else:
            print(f"Hello {user}, thank you for logging again")


# Q 5-10. Checking Usernames: Do the following to create a program that simulates 
# how websites ensure that everyone has a unique username.
# •	Make a list of five or more usernames called current_users.
# •	Make another list of five usernames called new_users. Make sure one or 
# two of the new usernames are also in the current_users list.
# •	Loop through the new_users list to see if each new username has already 
# been used. If it has, print a message that the person will need to enter a 
# new username. If a username has not been used, print a message saying 
# that the username is available.
# •	Make sure your comparison is case insensitive. If 'John' has been used, 
# 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of 
# current_users containing the lowercase versions of all existing users.)


current_users = ['admin', 'michle', 'saniya', 'elon', 'suraj']

new_users = ['sophea', 'mark', 'charles', 'simon', 'suraj']

current_users_lower = [user.lower() for user in current_users] # this lines helps to transper all the user into lower case

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"User name {new_user} is alredy available in the database, You need to enter new username")
    else:
        print(f"User name {new_user} is available, You may proceed")


# Q 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such 
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# •	Store the numbers 1 through 9 in a list.
# •	Loop through the list.
# •	Use an if-elif-else chain inside the loop to print the proper ordinal end
# ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 
# 7th 8th 9th", and each result should be on a separate line.


numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    elif number == 4:
        print("4th")
    elif number == 5:
        print("5th")
    elif number == 6:
        print("6th")
    elif number == 7:
        print("7th")
    elif number == 8:
        print("8th")
    elif number == 9:
        print("9th")



# Q 5-12. Styling if statements: Review the programs you wrote in this chapter, and 
# make sure you styled your conditional tests appropriately.


# Ans: i got through the each and evry lines of the codes and where it needed to be styling i did that 


# 5-13. Your Ideas: At this point, you’re a more capable programmer than you 
# were when you started this book. Now that you have a better sense of how 
# real-world situations are modeled in programs, you might be thinking of some 
# problems you could solve with your own programs. Record any new ideas you 
# have about problems you might want to solve as your programming skills con
# tinue to improve. Consider games you might want to write, data sets you might 
# want to explore, and web applications you’d like to create.


# Honestly at this point i am not able to handle the datasets but if i want to analyze it manually that is something which I'm able to do it
