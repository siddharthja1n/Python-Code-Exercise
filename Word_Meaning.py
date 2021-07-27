"""
Create a dictionary and take input from user and
return the meaning of the word from the dictionary
"""


dict_meaning = {"mutable":"liable to change",
                "immutable":"unable to be changed",
                "ordered":"organize and systematize",
                "unordered":"not organized or put in order"}
input_user = input("Enter a word to search its meaning: ")
print(f"The meaning of {input_user} is {dict_meaning[input_user]}")
