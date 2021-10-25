# Exercise 11 tut 97 CWH Python

#Regular Expression regex
# extract email from a string and list them

import re

mystr = '''
siddharth@email.com : email
siddharth123@email.com : email
address 
siddharth123-jain@email.com : email
fname1.lname2@email.com : username
address
username+10@yahoo.com : 
username0@yahoo.co.in
user_name01@gmail.com
username@yahoo.yahoo
'''

patt = r'[A-Za-z0-9._+%\-]+@[A-Za-z0-9._\-]+\.[A-Z|a-z]+\b'

emails = re.findall(patt, mystr)
for email in emails:
    print(email)