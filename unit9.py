# Class

class Student:

    #default constructors (constructor that create by default if you created or not that dont mind the python itself created it)
    def __init__(self):   #The self parameter is a reference to the current instance of the class, and  is used to access variable that belongs to the class.
        pass

    # parameterized constructors
    def __init__(self, fullname, marks):   #The self parameter is a reference to the current instance of the class, and  is used to access variable that belongs to the class.
        self.name = fullname
        self.marks = marks
        print(self)
        print("Adding the new student in the college database")



s1 = Student("Suraj Bhan", 97)
print(s1.name, s1.marks)

s2 = Student("Shivam", 87)
print(s2.name, s2.marks)
# print(s1.name)


# class Cars:
#     brand = "Range Rover"
#     price = "1 cr"


# c1 = Cars()
# print(c1.brand,"\n", c1.price)




#Attributes

