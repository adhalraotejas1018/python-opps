# method overridding
# assume we have two classes
# child class inherits from parent class
# and both class have same method-> A() with same arguments
# while calling A() method with child class object
# it override the parent class methos

class parent:
    def A(self):
        print("i am from Parent class")


class child(parent):
    def A(self):
        print("i am from  CHILD class ")

obj=child()
obj.A()
