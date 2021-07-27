# Guess the Number ---- Exercise 3
# Total number of guesses allowed is 5
# Print the number of guesses left
# Print you won or you lose
# Print number of guesses taken to finish

n = 18
i = 5
while(i):
    num = int(input("Guess the Number: "))
    i -= 1
    if num < n:
        print(f"The number is greater than {num}")
        print(f"{i} guess left\n")
    elif num > n:
        print(f"The number is less than {num}")
        print(f"{i} guess left\n")
    else:
        print(f"Congatulations!! You guessed correct number\nYou took {5-i} chance\nYOU WON")
        break
else:
    print("GAME OVER")
    print(f"The number is {n}")