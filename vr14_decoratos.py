# decorators->
# with the decorators we can perform the same task with different function
# decorators takes in function adds some functionality and return it
# syntax of decorators
# @function_name


def my_function(func):
    def function_start():               # this is another function
        print("function started ")
        func()                            #this si function which taken as a arguments
        print("function ended")
    return function_start()               #we return the fuction because for calling the function which we return

@my_function
def myself():                                # this us simple function which we pass as a arguments
    print("my name is Virat 18")


# @my_function ------> means call myself() like ->>
# myself=my_function(myself)