# Exercise 2 : faulty calculator
# 45*3=555, 56+9=77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except the faulty ones above


operator = input("Enter an operator from \(+,-,*,\): ")
var1 = int(input("Enter first number: "))
var2 = int(input("Enter second number: "))
if operator == '-':
    print(f"The difference of {var1} and {var2} is {var1 - var2}")
elif operator == "*":
    if var1 == 45 and var2 == 3:
        print("The multiplication of 45 and 3 is 555")
    else:
        print(f"The multilication of {var1} and {var2} is {var1 * var2}")
elif operator == "+":
    if var1 == 56 and var2 == 9:
        print("The sum of 56 and 9 is 77")
    else:
        print(f"The sum of {var1} and {var2} is {var1 + var2}")
else:
    if var1 == 56 and var2 == 6:
        print("The division of 56 and 6 is 4")
    else:
        print(f"The division of {var1} and {var2} is {var1 / var2}")