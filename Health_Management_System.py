# Health Management System
# 3 clients- Harry, Rohan and Hammad
def getdate():
    import datetime
    return datetime.datetime.now()
# total 6 files
# Write a function that when executed takes as input client name
# one more function to retrieve exercise or food for any client

clients = ["Harry", "Rohan", "Hammad"]
length = len(clients)

def log(client, f_e):
    if f_e == 1:
        name = clients[client-1] + "Food.txt"
        print("Enter Food:")
    else:
        name = clients[client-1] + "Exercise.txt"
        print("Enter Exercise:")
    with open(name, "a") as f:
        add = input()
        time = "[" + str(getdate()) + "] "
        f.write(time + add + "\n")

def retrieve(client, f_e):
    if f_e == 1:
        name = clients[client-1] + "Food.txt"
    else:
        name = clients[client-1] + "Exercise.txt"
    with open(name) as f:
        for line in f:
            print(line)

log_retrieve = int(input("What do you want?\n"
                         "Press 1 to Log\n"
                         "Press 2 to Retrieve\n"))
if log_retrieve not in (1, 2):
    print("Incorrect input")
    exit()

for i in range(length):
    print(f"Press {i+1} for {clients[i]}")
client = int(input())
if client not in (1, 2, 3):
    print("Incorrect input")
    exit()

food_exercise = int(input("What do you want?\n"
                          "Enter 1 for Food\n"
                          "2 for Exercise\n"))
if food_exercise not in (1, 2):
    print("Incorrect input")
    exit()

if log_retrieve == 1:
    log(client, food_exercise)
else:
    retrieve(client, food_exercise)