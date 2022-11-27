# Hybrid Inheritance is the mixture of two or more different types of inheritance.
# Here we can have many to many relations between parent classes and child classes

class School:
    def func1(self):
        print("This function is in school.")


class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


# Driver's code
object = Student3()
object.func1()
object.func2()
# object.func3()
object.func4()