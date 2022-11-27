# there are basically three types of acess apecifier
# 1)public - you can acess/use anywhere
# 2)protected - you can acess by only derived class or that class .defined using _ at the beginning of variable name.
#              ex.  _name="Rutvik"
# 3)private - you can acess by only that class object .defined using __ at the beginning of variable name.
#              ex.  __age=1018

class school:
    name="Rutvik school"
    _pincode=18
    __password=1018

class student(school):
    def prt_password(self):
        print("my name is ",self.name)
        print("my password is ",self.__password)      # this contain error ,because we cannot use the private variable in derived class


v=school()
r=student()

# way to acess the variables by that class object
print(v.name)
print(v._pincode)
print(v._school__password)

# acess variable by the derived class object
print(r.name)
print(r._pincode)
r.prt_password()