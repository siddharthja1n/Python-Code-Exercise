# Tut 81 Exercise 8 Oh soldier prettify my folder

# Inputs - path, dictionary file, format
# take 3 inputs from user,
# path of the folder,
# a txt file which contains names of files which should not be renamed
# format/extension of the file which names should be serially, e.g : for jgp format - 1.jpg, 2.jpg and so on.....
# capitalize rest of the file names


import os

def soldier(path, directory_file, format):
    i = 0
    with open(directory_file) as f:
        dont_rename_file = f.read().splitlines()
    list_files = os.listdir(path)

    for old_name in list_files:
        if old_name not in dont_rename_file:
            if format in old_name:
                i += 1
                new_name = str(i)+format
            else:
                new_name = old_name.capitalize()
            os.renames(old_name, new_name)

if __name__ == "__main__":
    path = input("Enter path: ")
    dictionary_file = input("Enter dictionary file name(with extension): ")
    format = input("Enter format (e,g - .jpg): ")
    soldier(path, dictionary_file, format)
    print("Successfully prettified")