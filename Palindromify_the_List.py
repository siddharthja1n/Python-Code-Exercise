# Practice problem 5 tut 112 CWH Python

# Palindromify the List

'''
You are given a list that contains some numbers.
You have to print a list of the next palindromes
only if the number is greater than 10,
otherwise, you will print the same number.
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

if __name__ == '__main__':
    try:
        numbers = list(map(int, input("Enter space separated list of numbers\n"). split()))
    except:
        print("Invalid input!")
        exit()

    palindromify = []

    for num in numbers:
        if num > 9:
            palindromify.append(next_palindrome(num))
        else:
            palindromify.append(num)

    print("List of palindrome numbers:")
    print(palindromify)
