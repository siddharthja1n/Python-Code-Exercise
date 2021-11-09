# Practice problem 4 tut 110 CWH Python

# Next palindrome
'''
You have to take a number as an input from the user.
You have to find the next palindrome
corresponding to that number.
Your first input should be the number of test cases
and then take all the cases as input from the user.

Output:
Next palindrome for 451 is 454
Next palindrome for 10 is 11
'''

def next_palindrome(num):
    '''
    Function to find next palindrome for the given parameter
    :return: next palindrome
    '''
    n = num + 1
    while(True):
        if str(n) == str(n)[::-1]:
            return n
        else:
            n += 1

if __name__ == "__main__":
    numbers = []
    try:
        testcases = int(input("Enter number of Test cases you want to run:\n"))

        for i in range(testcases):
            numbers.append(int(input("Enter the number to find next palindrome\n")))
    except:
        print("Invalid input!")

    for num in numbers:
        next = next_palindrome(num)
        print(f"Next palindrome for {num} is {next}")