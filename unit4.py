magicians = ['alice', 'bob', 'david', 'carolina']
for maigician in magicians:
    print(maigician)


for magician in magicians:
    print(f"{magician.title()} you performed a great trick")
    print(f"I can't wait to see your next tric,{magician.title()}\n")

print("Thank you everyone, It was a great magic show")


magicians = ['alice', 'bob', 'david']
for magician in magicians:
    print(magician)



# Q 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these 
# pizza names in a list, and then use a for loop to print the name of each pizza.
# •	Modify your for loop to print a sentence using the name of the pizza 
# instead of printing just the name of the pizza. For each pizza you should 
# have one line of output containing a simple statement like I like pepperoni 
# pizza.
# •	Add a line at the end of your program, outside the for loop, that states 
# how much you like pizza. The output should consist of three or more lines 
# about the kinds of pizza you like and then an additional sentence, such as 
# I really love pizza!

pizzas = ['flamming chicks', 'chicken lugs', 'hawallan classic']
for pizza in pizzas:
    print(f"I like perpperoni pizza, {pizza}")

print(f"i like pizza particularly moshroom pizza it's good for the health too")


# Q 4-2. Animals: Think of at least three different animals that have a common char
# acteristic. Store the names of these animals in a list, and then use a for loop to 
# print out the name of each animal.
# •	Modify your program to print a statement about each animal, such as 
# A dog would make a great pet.
# •	Add a line at the end of your program stating what these animals have in 
# common. You could print a sentence such as Any of these animals would 
# make a great pet!

animals = ['dog', 'cat','parrot']
for animal in animals:
    print(f"A {animal}, would make a great pet")

print(f"{animals[0]}, is a great pet")


# now list with numbers

for value in range(1, 5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)


squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)

# make it more concise 
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)


# statics with the list of numbers 

digits = [1,2,3,4,5,6,7,8,9]
print(min(digits))
print(max(digits))
print(sum(digits))

numbers = range(1,11)
print(min(numbers))
print(max(numbers))
print(sum(numbers))


# list comprehensions

squares =   [values ** 2 for values in range(1,11)]
print(squares)


# Q 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, 
# inclusive.

for value in range(1,21):
    print(value)

# Q 4-4. One Million: Make a list of the numbers from one to one million, and then 
# use a for loop to print the numbers. (If the output is taking too long, stop it by 
# pressing ctrl-C or by closing the output window.)

numbers = list(range(1,1000001))
# print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))


# Q 4-6. Odd Numbers: Use the third argument of the range() function to make a 
# list of the odd numbers from 1 to 20. Use a for loop to print each number.

for value in range(1,20, 2):
    print(value)


# Q 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to 
# print the numbers in your list.

threes = [value *3 for value in range(3,30)]
print(threes)

print('\n')

# Q 4-8. Cubes: A number raised to the third power is called a cube. For example, 
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that 
# is, the cube of each integer from 1 through 10), and use a for loop to print out 
# the value of each cube.

cubes = []
for value in range(1,11):
    cube = value **3
    cubes.append(cube)

print(cubes)

print('\n')
# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the 
# first 10 cubes.

cubes = [value **3 for value in list(range(1,11))]
print(cubes)


players = ['charles', 'martina', 'michale', 'florence', 'eli']
print(players[0:3])

print(players[1:4])
print(players[:4]) # starting position is not defined that means it will start with begining
print(players[2:])

print(players[-3:])

print(f"Here is the first three players in my team")
for player in players[:3]:
    print(player.title())

print(players[:])

#copying list one into another

my_food = ['pizza', 'flafel', 'Carrot cake']
# frnd_food = my_food[:]

my_food.append('cannoil')
frnd_food = my_food[:]
frnd_food.append('Ice cream')

print(f"My favourite foods are: {my_food}")
print(f"My friends favourite foods are {frnd_food}")


# Q 4-10. Slices: Using one of the programs you wrote in this chapter, add several 
# lines to the end of the program that do the following:
# •	Print the message The first three items in the list are:. Then use a slice to 
# print the first three items from that program’s list.
# •	Print the message Three items from the middle of the list are:. Use a slice to 
# print three items from the middle of the list.
# •	Print the message The last three items in the list are:. Use a slice to print the 
# last three items in the list.


players = ['charles', 'martina', 'michale', 'florence', 'eli']

print("Here are the first three item are in the list")
print(players[:3])

print("here are the items that  are present in the middle of the list")
print(players[1:4])

print("Here are the three items that are present in the last of my list")
print(players[-3:])


# Q 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. 
# Then, do the following:
# •	Add a new pizza to the original list.
# •	Add a different pizza to the list friend_pizzas.
# •	Prove that you have two separate lists. Print the message My favorite 
# pizzas are:, and then use a for loop to print the first list. Print the message 
# My friend’s favorite pizzas are:, and then use a for loop to print the sec
# ond list. Make sure each new pizza is stored in the appropriate list.

pizzas = ['flamming chicks', 'chicken lugs', 'hawallan classic']
frnd_pizzas = pizzas[:]

pizzas.append('veg pizza')
frnd_pizzas.append('cheese pizza')

print(f"My favourite pizza are: ")
for pizza in pizzas:
    print(pizza)

print("my friendds favourite list of pizzas are: ")
for frnd_pizza in frnd_pizzas:
    print(frnd_pizza)

# Tupple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])



print(dimensions[0])


my_t = (3,)
print(my_t)

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)


# Q 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five 
# simple foods, and store them in a tuple.
# •	Use a for loop to print each food the restaurant offers.
# •	Try to modify one of the items, and make sure that Python rejects the change.
# •	The restaurant changes its menu, replacing two of the items with different 
# foods. Add a line that rewrites the tuple, and then use a for loop to print 
# each of the items on the revised menu.

foods = ('pizza', 'burger', 'sandwich', 'Do-nut', 'briyani')

for food in foods:
    print(food)

# foods[1] = ('hot cheese')


foods = ('pizza', 'veg briyani', 'sandwich', 'mandi', 'briyani')

for food in foods:
    print(food)



