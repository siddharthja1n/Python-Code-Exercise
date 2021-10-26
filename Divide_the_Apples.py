# Practice Problem 2 tut 106 CWH Python

# Divide the Apples

'''
Harry Potter has got the “n” number of apples. 
Harry has some students among whom he wants 
to distribute the apples. 
These “n” number of apples is provided to harry
by his friends, and he can request 
for few more or a few less apples.

You need to print whether a number is in range
mn to mx, is a divisor of “n” or not.
'''

try:
    apples = int(input("Enter number of apples: "))
    mn = int(input("Enter minimum(mn) number of students: "))
    mx = int(input("Enter maximum(mx) number of students: "))
except:
    print("Invalid input :( better luck next time.")
    exit()

if mn == mx:
    print("mn is equal to mx")
elif mx < mn:
    print("mx should be greater than mn, exiting....")
    exit()

for i in range(mn, mx + 1):
    if apples%i == 0:
        print(f"{i} is divisor of {apples}")
    else:
        print(f"{i} is not a divisor of {apples}")
