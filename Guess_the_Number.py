# Practice problem 6 tut 114 CWH Python

# Guess the Number

'''
a and b are 2 integers taken as input from the user.
Generate a random integer between a and b(both exclusive.
You and your friend have to guess a number between a and b.
Your friend is player 1 and plays first.
He will have to keep choosing the number,
and your program must tell
whether the number is greater than or less than the actual number
Log the number of trials it took your friend to arrive at the number.
You play the same game,
and then the person with the minimum number of trials wins!
'''

import random

def check_num(n, actual):
    nguess = 1
    while(n != actual):
        nguess += 1
        if n < actual:
            print(f"Actual number is greater than {n}")
        else:
            print(f"Actual number is less than {n}")
        try:
            n = int(input("Now guess the number:\n"))
        except:
            print("Invalid Input! Exiting...")
            exit()
    print(f"\nCorrect! The actual number is {n}\n"
          f"You took {nguess} trials")
    return nguess

if __name__ == '__main__':
    try:
        a = int(input("Enter the value of a:\n"))
        b = int(input("Enter the value of b:\n"))
        # players = int(input("Enter the number of players:\n"))
        # by default taking number of players as 2
        players = 2
    except:
        print("Invalid Input! Exiting...")
        exit()

    no_of_trials = []

    for i in range(1, players + 1):
        actual = random.randint(a + 1, b - 1)
        print(f"\nPlayer{i}:\n")
        try:
            n = int(input(f"Please guess the number between {a} and {b}\n"))
        except:
            print("Invalid Input! Exiting...")
            exit()
        no_of_trials.append(check_num(n, actual))

    print(f"\nPlayer{no_of_trials.index(min(no_of_trials)) + 1} won!")


