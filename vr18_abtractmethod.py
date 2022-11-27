#Abstraction ->> Abstraction in python is defined as a process of handling complexity by
# hiding unnecessary information from the user.
# @abstactmethod ->
# you can define the class a with @abstactmethod
# class a contain printdetails() method with @abstactmethod
# that means
# all subclasses of the class A must have printdetails() method
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod               #abstract method  printarea
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):                 #subclass with printarea
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

