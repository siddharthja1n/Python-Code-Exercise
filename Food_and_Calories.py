# Practice problem 3 tut 108 CWH Python

# Food and Calories
'''
You visited a restaurant, and the food items
in that restaurant are sorted,
based on their amount of calories.
You have to reserve this list of food items
containing calories.

You have to use the following three methods to reserve
a list and print all of them and compare them:

1. Inbuild method of python
2. List name [::-1] slicing trick
3. Swap the first element with the last one and second element with second last one and so on
'''

def rev_inbuild(calories):
    # to create copy with different memory location
    calo = calories[:]
    calo.reverse()
    return calo

def rev_slicing(calories):
    calo = calories[:]
    return calo[::-1]

def rev_swap(calories):
    calo = calories[:]
    length = len(calo)
    half = length // 2
    for i in range(0, half):
        calo[i], calo[length - i - 1] = calo[length - i - 1], calo[i]
    return calo

if __name__ == "__main__":
    try:
        cal = list(map(int, input("Enter sorted space separated amount of calories\n"). split()))
    except:
        print("Invalid input!")
        exit()

    rev1 = rev_inbuild(cal)
    print(rev1)
    rev2 = rev_slicing(cal)
    print(rev2)
    rev3 = rev_swap(cal)
    print(rev3)

    if rev1 == rev2 and rev2 == rev3:
        print("All three methods give the same results!")
    else:
        print("Something went wrong!")

