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

