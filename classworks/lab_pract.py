#python basic practice lab

#1.    Variables,   types &     operators


#example: 1
# Integer Values:
def Student(name, age, gpa):
    print(f"My name is {name}")     #string
    print(f"I am {age} Years old")  #int
    print(f"And my gpa is {gpa}")   #float


Student("Suraj Bhan", 19, 9.3)




#example: 2
#Arithmetical Operations
def Arithmetic_op(A, B):
    print("Addition: ", (A+B))
    print("Subtraction: ", (A-B))
    print("Floor Division ", (A//B))
    print("Modulus: ", (A%B))
    print("Exponent: ", (A**B))

Arithmetic_op(10, 29)



#example: 3
# Logical and Assignment Operator


def Logical_assi(a, b):
    print(a > b and b > 10)
    print(b > a and a > 10)

    result = a+b
    print(result, type(result))

Logical_assi(30, 20)






#Strings and f-strings

# Example: 1
#Basic creation, indexing and slicing

message = "Hello Mr. Suraj Bhan"

print(message[0])       #printing first letter
print(message[-1])      #last character
print(message[:])       #whole value
print(message[4:11])    #From the given index to the particular index
print(message.upper())  #Upper case
print(message.lower())  #lower case



# Example: 2
#Common string method

sentence = "Python is fun and powerful"
print(repr(sentence.strip()))       #remove leading/trailling whitespace
print(sentence.strip().split())     #split into a list of words
print("-".join(["2026", "07", "07"]))   #join a list into a string
print(sentence.replace("fun", "awesome").strip())



#Example: 3
# f"" strings for readable formating 
name = "Suraj Bhan"
score = 91.678
subject = 8



print(f"Hello, {name}! You are enrolled in {subject} subjects.")
print(f"Your average score is {score:.2f}%")    #decimal points
print(f"{name.upper()} scored {score:.2f} out of 100") # expression + method call inside f-strings
print(f"{'PASS' if score >= 40 else 'FAIL'}")   #Conditional expression inside f-string
 


# 3. Lists
# Creating a list and a basic example
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")  #adding one element into list
fruits.insert(1, "kiwi")
print(fruits)
print("Length:", len(fruits))
print ("First Item: ", fruits[0])
print("Last two items:", fruits[-2:])



# Example: 2
#list comprehension

numbers = [2,3,4,5,6,9,5,3,]
squares = [n ** 2 for n in numbers]     #list comprehension
even_square = [n ** 2 for n in numbers if n%2 == 0]


print("Original Numbers: ", numbers)
print("Square of a number: ", squares)
print("Even Square", even_square)
print("Sorted in assending order", sorted(numbers))
print("Sorted in Decending orders", sorted(numbers, reverse=True))



#Nested list and common list methods
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

print("Element at row 1 and col 2 is:", matrix[0][1])


scores = [88,45,76,92,33]
scores.remove(45)

print("After removing 45: ", scores)

print("Max:", max(scores), "|Min: ", min(scores), "|Sum: ", sum(scores))



# Tuples and Unpacking

#Exapmle: 2

#creating tuple and basic unpacking

point = (4,7)
x, y = point
print(f"x = {x}, y = {y}")


rgb= (255, 99, 71)
print("RGB tuple: ", rgb, type(rgb))



#Example: 2
#tuple immutablity and multiple-return-value unpacking
def min_max(values):
    return min(values), max(values)

lowest, highest = min_max([12, 45, 3, 67, 21])
print(f"lowest {lowest}, highest {highest}")

try:
    rgb = (255, 99, 0)
    rgb[0]=0
except TypeError as e:
    print("Error: ", e)



# Extended unpacking with the * operator
scores = (88, 92, 76, 65, 99, 71)
first, second, *rest = scores

print("First: ", first)
print("Second: ", second)
print("Rest: ", rest)

*begnings, last = scores
print("Begining: ", begnings)
print("Last: ", last)





#Loops: 'for', 'range', 'enumerate'
# Basic foor loop over a list, and looping with range()

fruits = ["Apple", "Banana", "cheery"]
for fruit in fruits:
    print("I like ", fruit)


print("---")
for i in range (1, 6):
    print("Number: ", i)




#Example: 2
# range() with a step over a looping over a string

for i in range (0, 20, 5):  # start=0, end: 20, step:5
    print(i, end="")
print()

for ch in "python":
    print(ch, end="-")
print()



#Example: 3
#Enumarate with a custom start value


for index, fruit in enumerate(fruits, start=1):
    print(f"Items {index} -> {fruit}")