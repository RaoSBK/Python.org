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