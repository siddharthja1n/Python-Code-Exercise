#astrologers stars, pattern printing---- exercise 4
# input int n
# boolean variable

# true n = 5
# *
# * *
# * * *
# * * * *
# * * * * *
#
# false n =4
# * * * *
# * * *
# * *
# *

star = "* "
n = int(input("Enter number of lines you want: "))
binary = int(input("Enter 0 for downward or 1 for upward triangle: "))
if binary:
    for i in range(n):
        print(star*(i+1))
else:
    for i in range(n):
        print(star*(n-i))