# tut 72 mini project 1
# Library management system

# create library class:
# Library(list of book, name of library)
# 4 methods:
# display book
# lend book - (who owns the book if not in library)
# add book
# return book

# lend - dictionary (books:nameofperson)

# create a main function and run an infinite while loop
#     asking users for their input

class CentralLibrary:
    dictLendBooks = dict()

    def __init__(self, listBook, name):
        self.listBook = listBook
        self.name = name

    def display_book(self):
        print("List of books available in the library")
        for book in self.listBook:
            print(book)

    def lend_book(self, book):
        if book not in self.listBook:
            print("This book is not present in our library (you can donate by adding book) or check for spelling mistake and try again!")
        else:
            user = input("Enter your name: ")
            CentralLibrary.dictLendBooks[book] = user
            self.listBook.remove(book)
            print(f"You can collect your book {book}")

    def add_book(self, book):
        if book in self.listBook:
            print("Book is already present in the library")
        elif book in CentralLibrary.dictLendBooks:
            print(f"Book is present in the library but is currently borrowed by {CentralLibrary.dictLendBooks[book]}")
        else:
            self.listBook.append(book)

    def return_book(self, book):
        if book in CentralLibrary.dictLendBooks:
            self.listBook.append(book)
            CentralLibrary.dictLendBooks.pop(book)
            print("Thanks for returning our book")
        else:
            print("You haven't borrowed this book from our library")

if __name__ == "__main__":
    reader = CentralLibrary(["Python", "Harry potter", "Think and grow rich", "Let us c", "Alchemist"], "e-Library")
    print(f"Welcome to {reader.name}")

    while True:
        userChoice = input("1 to 'Display books available in the library':"
                            "\n2 to 'Lend a book':"
                            "\n3 to 'Donate book to library':"
                            "\n4 to 'Return issued book':\n")
        if userChoice not in ("1", "2", "3", "4"):
            print("Invalid input....Try again!!")
            continue

        if userChoice == "1":
            reader.display_book()

        elif userChoice == "2":
            bookLend = input("Enter name of the book you want to borrow: ")
            bookLend = bookLend.capitalize()
            if bookLend in CentralLibrary.dictLendBooks.keys():
                print(f"{bookLend} is already borrowed by {CentralLibrary.dictLendBooks[bookLend]}. Lend another book now!!")
            else:
                reader.lend_book(bookLend)

        elif userChoice == "3":
            bookDonate = input("Enter the name of the book you want to donate: ")
            bookDonate = bookDonate.capitalize()
            reader.add_book(bookDonate)

        else:
            bookReturn = input("Enter the name of the book you want to return: ")
            bookReturn = bookReturn.capitalize()
            reader.return_book(bookReturn)

        quitOrContinue = input("Press q if you want to quit or any key if you want to continue: ")
        if quitOrContinue == "q":
            exit()
        else:
            continue