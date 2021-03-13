# -------------------------- Library Management System ----------------- #
"""
Create a library class -
------------------ methods ---------------
display_book = for displaying all books in library
lend_book = for lend book  - Lend means give something to someone for a short time, expecting that you will get it back
lend_book (if book is not available print who have the book currently )
add_book  = if someone donate a book add that book in library
return_book = to returning a book to some one

------------- Constructor -----------------
sherry_library = Library([list_of_books], library name)

dictionary = {book_name:person name who have this book}

Create a main func and run an infinite loop asking the user for their input
"""

list_of_books = ['Python Crash Course', 'Learn Version Control With Git', 'Smarter Way to Learn Python', 'Manning DL']


class Library:

    def __init__(self, books_list, library_name):
        self.Books = books_list
        self.Library_name = library_name
        self.lendDict = {}

    def display_books(self):
        return f'Welcome to {self.Library_name}, The Books available in our library are {self.Books}\n'

    def lend_books(self, book, user):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print(f"Dictionary has been Updated You can take your Book {book} now.")
        else:
            print(f"Sorry Sir book is already in use of {self.lendDict[book]}")

    @staticmethod
    def add_book(user, book):
        print(f"{user} sir we appreciate your effort for our library.")
        list_of_books.append(book)
        print(f'Thank you {user} have a nice day :)')

    def returning_book(self, book_name):
        if book_name in list_of_books:
            self.Books.remove(book_name)
            print(f"{book_name} has been removed.")
        else:
            print(f"{book_name} is not in our Library.")


def main():
    while True:
        lib_name = input("Enter name for library -")
        user = Library(list_of_books, lib_name)

        def user_inp_for_library():
            ask_inp = input(f'What do you want to do in {lib_name} ? For list of books press "books", for lend a book '
                            f'press "lend" for donating a book press "donate" & for accessing a book press'
                            f' "return". \n').upper()
            if ask_inp == 'BOOKS':
                print(user.display_books())
            elif ask_inp == 'LEND':
                name = input("Enter your name: ")
                book_name = input('Enter the name of book which you want to lend: ')
                print(user.lend_books(book_name, name))
            elif ask_inp == 'DONATE':
                name = input("Enter your name: ")
                book = input("Enter book name: ")
                print(user.add_book(name, book))
            elif ask_inp == 'RETURN':
                ret_book = input(f"Enter the book name which you want.")
                print(user.returning_book(ret_book))
            else:
                print('Invalid Input')

        user_inp_for_library()

        def again():
            ask = input('Do you want to continue with your Library ? press Y/N -  \n').upper()
            if ask == 'Y':
                user_inp_for_library()
            else:
                pass

        again()


main()
