# Practice Problem 1 tut 104 CWH Python

# Age in 2050
'''
Take age or year of birth as an input from the user.
Store the input in one variable.
Your program should detect
whether the entered input is age or year of birth
and tell the user when they will turn 100 years old.
'''

# Users can optionally provide a year,
# and your program must tell their age in that particular year.

# current year is 2021

x = 1
while(x):
    try:
        age_yob = int(input("Enter your Age/Year of Birth: "))
        x = 0
    except:
        print("Invalid input :( Please enter a valid number")

year = 2021
yob = 2021

if age_yob > 0 and age_yob <= 100:
    yob = year - age_yob

elif age_yob >= year - 100 and age_yob <= year:
    yob = age_yob

elif age_yob > 100 and age_yob < year - 100:
    print("You seem to be the Oldest Person Alive ;)")
    exit()

else:
    print("You are NOT born yet :)")
    exit()

print(f"You will hit century in {yob + 100} ;)")

print(f"You will be {2050-yob} years old in 2050\n")
try:
    know_age = int(input("Do you want to know your age in: "))
except:
    print("Invalid input :(")
    exit()

if know_age > year:
    print(f"You will be {know_age - yob} years old in {know_age}")
elif know_age > yob:
    print(f"You were {know_age - yob} years old in {know_age}")

else:
    print("Invalid input :(")