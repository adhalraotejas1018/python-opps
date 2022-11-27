# @staticmethod-> static method with decorator
# we know that the simple method in class take self as first argument automatically
# also in @classmethod  function take 'class' as first element automatically
#### but in the @staticmethod is deoes not take any argument automatically

# we can use or call  static method function with class object or class

class A:
    v=18
    name="Rutvik"

    def prt_info(self):                                         #simple class method with aarguments
        print(f"i am {self.v} and my name is {self.name}")

    @staticmethod
    def prt_intro():                                            #static method with no argument
        print("hi good morning my name is ViRat")

obj1=A()
obj1.prt_intro()
A.prt_intro()


