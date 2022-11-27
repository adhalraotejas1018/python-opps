# __init()__ -  fuction is same as constructor
# this method basically use for the assigning the values
# __init()__ - this method code always execute with class code

class Person:
    def __init__(self, name,roll_num):
        self.name = name
        self.roll_num = roll_num
        print("    init method code execute.....! ")

    # Sample Method
    def print_info(self):
        print('Hello, my name is', self.name)
        print('my roll number is the ',self.roll_num)

    def say_hi(self):
        print("hiii .... good morning",)

v = Person("ViRat",18)
v.print_info()
v.say_hi()
