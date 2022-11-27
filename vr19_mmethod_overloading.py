# Overloading is the ability of a function to behave in different ways
# based on the parameters that are passed to the function,
# ******************
# method overloading -> multiple methods same name with different parameter

def area( x = None, y = None):
        if x != None and y != None:
            return x * y
        elif x != None:
            return x * x
        else:
            return 0

print("Area Value:", area())
print("Area Value:", area(4))
print("Area Value:", area(3, 5))