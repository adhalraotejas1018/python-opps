# object =>>
# we can access class methods using calss object
# when we define a class its needs to create an object to allocate the memory

class Student:
    def print_name(self):
        print("my name is -->>  ViRat18")
        print("Good Moring ....! ")


Rutvik=Student()                 #creating the class object -Rutvik
Rutvik.print_name()             #calling the class method