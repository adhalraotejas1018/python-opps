import re
input2 = 'my contact number is 1111 and my emergency contact number is 2222'

text=r'[0-9]+'
rv=re.findall(text,input2)

my_dict={}

my_dict["primary_number"]=[rv[0]]
my_dict["emergency_number"]=[rv[1]]

print(my_dict)
