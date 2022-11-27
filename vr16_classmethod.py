# Class Methods As Alternative Constructors --> we use for the setiing values of class variables
class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def Set_val(cls, string):
        mystr = string.split("-")                          #spliting the string
        print(mystr)                                       #printinhg the string
        return cls(mystr[0], mystr[1], mystr[2])         #return value to class ,set value after splitting


harry = Employee("Harry", 255, "Instructor")
karan = Employee.Set_val("Karan-480-Student")            #passing the string to from_dash

print(karan.printdetails())



