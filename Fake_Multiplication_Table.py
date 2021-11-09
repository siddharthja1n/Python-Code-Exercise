# Practice problem 8 tut 118 CWH Python

# Fake Multiplication Table

'''
A candidate is a fraud by nature.
He wrote a python function to print a multiplication table
of a given number and put one of the values (randomly generated) as wrong.

He did this to fool his classmates and make them commit mistake in a test.
You cannot tolerate this!
So you decided to use your python skills to counter
his actions by writing a python program that validates his multiplication table.

Your function should be able to find out the wrong values
in his table and expose him as a fraud.

Note: His function returns a list of numbers like this

Sam’s Function Input:
samMultiplication(6)

Sam’s function returns this output:
[6, 12, 18, 26,..., 60]

You have to write a function isCorrect(table, number)
and return the number where Sam’s function is wrong
and print it to the screen! If the table is correct, your function returns None
'''

import random

def samMultiplication(n):
    samTable = [i*n for i in range(1,11)]
    wrong = random.randint(1,8)
    samTable[wrong] += random.randint(0,5)
    return samTable

def isCorrect(n, table):
    for i in range(1,11):
        if n*i != table[i-1]:
            return i - 1
    return None

if __name__ == '__main__':
    try:
        num = int(input("Enter a number to finds it's Multiplication Table\n"
                    "using method provided by Sam:\n"))
    except:
        print("invalid input! Exiting...")
        exit()

    samtable = samMultiplication(num)
    print(samtable)

    # check if Sam's table is correct
    wrongIndex = isCorrect(num, samtable)

    if wrongIndex is None:
        print("Table is correct")
    else:
        print(f"Table is wrong at index {wrongIndex}")
