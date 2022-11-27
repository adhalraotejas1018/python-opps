# The requests module allows you to send HTTP requests using Python
# Make a request to a web page, and print the response text:

import requests
x = requests.get('https://w3schools.com/python/demopage.htm')
print("printing the text of the web site",x.text)
print("\nprinting the satis code  of the program",x.status_code)
