# @classmethod -> class method decorator
# you cannot change the class variable  using the instance(object) of a class
# but using the class method decorator we define the fuction which automatically taken  class as first argument.
# and we define the function to change the variables of class by using the @classmethod

#@classmethod - it take  automaically class as  first argument

class A:
    v=18
    name="Rutvik"

    def prt_info(self):
        print(f"i am {self.v} and my name is {self.name}")

    @classmethod
    def change_val(cls,x):
        cls.v=x

obj1=A()
obj2=A()

# # obj1.v=1018             it change the v value for the obje1 only
# print(obj2.v)

# obj1.change_val(1018)        this change the value for the permently
print("new value ",obj1.v)
print("new value ",obj2.v)

