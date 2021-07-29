# Snake Water Gun Game

import random

life = 10
computer = 0
user = 0
choice = ["Snake", "Water", "Gun"]
print("Welcome to Snake Water Gun game")

while(life):

    computer_choice = random.choice(list(choice))
    print(f"You got {life} life")

    user_choice = int(input("Enter\n'1' for Snake.... "
                                    "'2' for Water.... "
                                    "'3' for Gun: \n"))

    if user_choice not in range(1,4):
        print("You entered incorrect input")
        print("Try again!!")
        continue
    life -= 1

    user_choice = choice[user_choice-1]
    if computer_choice == user_choice:
        print(f"You and Computer both chose {computer_choice}, so draw")
    elif computer_choice == choice[0]:
        if user_choice == choice[1]:
            print(f"Computer Chose {computer_choice}, so computer wins")
            computer += 1
        else:
            print(f"Computer Chose {computer_choice}, so you win")
            user += 1
    elif computer_choice == choice[1]:
        if user_choice == choice[2]:
            print(f"Computer Chose {computer_choice}, so computer wins")
            computer += 1
        else:
            print(f"Computer Chose {computer_choice}, so you win")
            user += 1
    else:
        if user_choice == choice[0]:
            print(f"Computer Chose {computer_choice}, so computer wins")
            computer += 1
        else:
            print(f"Computer Chose {computer_choice}, so you win")
            user += 1

    print(f"YOU - {user} ------------------ COMPUTER - {computer}")

print("GAME OVER\n")
if computer == user:
    print("Its a DRAW")
    print(f"You and computer both won {user} times")
elif computer > user:
    print("You LOSE")
    print(f"Computer won {computer} times, and you won {user} times")
else:
    print("You WIN")
    print(f"You won {user} times, and computer won {computer} times")
