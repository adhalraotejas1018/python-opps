# regular ecpression ->> it is a text matching patterns described with a formal syntax
# in simple words re is->> processing string and get string in the different way
# it is also known as the regx or regxp
#it basically used for finding/searching the text pattern in string
# some function of regular expression
#  search,match,sub,split,findall etc.
# lets learn the search() - it search the text in the string

import re                                                         #importing the regular expresssion
my_str="hi mr. Tejas adhalrao  goood marining brother  bye gn"   #this is the  simple string
text="hi"                                                        #this is text which you want to seach

v=re.search(text,my_str)                                         #we store it into variable


print(v)                                                        #printing the v
print(bool(v))                                                  #convert v into boolean  and print it



#one more example of search

print("\nanother example")
students="Virat Rutvik Tejas Dhoni Hardik"
name='Dhoni'
if re.search(name,students):                            #if name present in the students list then if code run otherwise else code run
    print("we found the student ")
else:
    print("we didint find the student")