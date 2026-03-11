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

