# most poweful features of opps in python
# inheritance -> process of inheriting the properties of parent(base) class to child(derived) class
# It provides the reusability of a code
# we can call  base(parent) class methods by derived(child) class object
# Inheritance is the process of creating a new class from an existing class
# The class that is inherited is known as the super/parent/base class, and the class that inherits is known as the sub/child/derived class.
# A derived class can access properties of the base class.

# types
# single inheritance
# multiple Inheritance
# multilevel Inheritance
# hybrid Inheritance
# Hierarchical Inheritance


#**** single inheritance
# Base class
class Parent:
    def func1(self):
        print("This method is in parent class.")


# Derived class
class Child(Parent):
    def func2(self):
        print("This method is in child class.")


# accessing the methods of both classes by child class object
obj1 = Child()
obj1.func1()
obj1.func2()
