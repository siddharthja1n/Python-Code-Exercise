# Practice problem 9 tut 120 CWH Python

# Jumbled Funny Names

'''
It's result day at school and not everyone is happy.
You decided to make your friends laugh by jumbling their names
to come up with some funny names.

Your program should take the number of names
and the names separated by space as input.
Output should be funny names in the same order.
'''

import random

if __name__ == '__main__':
    try:
        n = int(input("Enter number of names you want:\n"))
    except:
        print("Invalid input! Exiting...")
        exit()

    names = []
    for _ in range(n):
        names.append(input("Enter name:\n"))

    first_name = [] * n
    last_name = [] * n

    for i in range(n):
        first_name.append((names[i].split(" ", 1))[0])
        last_name.append((names[i].split(" ", 1))[1])

    print()
    for i in range(n):
        index_last = random.randint(0, n-1-i)
        print(first_name[i], last_name[index_last])
        last_name.pop(index_last)
