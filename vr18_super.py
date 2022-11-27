#super() it basically used to calll superclass constructor also used to pass value to superclass constructor
#it is very useful in  multiple and multilevel inheritances
# it is python inbuilt function

class Emp:
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add


# Class freelancer inherits EMP
class Fresher(Emp):
    def __init__(self, id, name, Add, Emails):
        super().__init__(id, name, Add)
        self.Emails = Emails


Emp_1 = Fresher(103, "RutVik", "ViRAt", "Viru1018@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)
