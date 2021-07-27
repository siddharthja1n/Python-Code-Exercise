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
    elif num > n:
        print(f"The number is less than {num}")
    else:
        print(f"Congatulations!! You guessed correct number\nYou took {5-i} chances\nYOU WON")
        break
    if i > 1:
        print(f"{i} chances left to guess the number\n")
    else:
        print(f"{i} chance left to guess the number\n")
    if i == 0:
        print("GAME OVER")
        print(f"The number is {n}")