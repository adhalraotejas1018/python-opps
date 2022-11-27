# re.match() searches only from the beginning of the string and return  object if match found.otherwise  it returns none.
# it checks only starts if substring found in middle of string then it return the none.
# it return the object when the it matches at beginning

import re
my_str="hiiiiee good morning ffavjn bai  vbudnu n duaofeic c woc "
text='hiiiiee'
text2='good'

v=re.match(text,my_str)
r=re.match(text2,my_str)
print(v)
print(r)

# split() ->> it is used to split the string and return the list
slpit_var="@"
string1="hi brother howw @ are you"

vr=re.split(slpit_var,string1)
print(vr)

# findall()-- it return a list of all matched instances/
txt="om"
str="hari om hari om hari om namo"

rv=re.findall(txt,str)
print(rv)






























































