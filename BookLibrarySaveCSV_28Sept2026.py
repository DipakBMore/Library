# Today;s Assignment (26th Sept): 

# write a python program mainly focusing on OOPS concepts.
# class BOOK and Class Library. 
# which should be able to add books by taking inputs from user, show books and borrow books.
# -> their can be more than one library
# -> same book can have multiple copies, one in each library
# -> note: please let me know if one can borrow the same book muliple times

# class Book:
#     def __init__(self,booktitle, bookauthor):   
#         self.booktitle = booktitle
#         self.bookauthor = bookauthor

#     def __str__(self):
#         return f"Book Name: '{self.booktitle}' Author: {self.bookauthor}"


# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books =[]
import csv
import os

CSV_Folder_Path = os.path.dirname(os.path.abspath(__file__)) #"D:\\DIPAK_AI_TRAINING\\GIFTABLED_AI_LEARN\\Programs"

#create class for Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

#create class for Library
class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}  # Dictionary: {Book: count}

#create functions to execute selected option in main.
    def add_book(self, book, count=1):
        if book in self.books:
            self.books[book] += count
        else:
            self.books[book] = count
        print(f"Added {count} copy(ies) of {book} to {self.name}.")

    def show_books(self):
        if not self.books:
            print(f"{self.name} has no books.")
            return
        print(f"\nBooks in {self.name}:")
        for book, count in self.books.items():
            print(f"{book} - {count} copy(ies)")

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title.lower() == book_title.lower():
                if self.books[book] > 0:
                    self.books[book] -= 1
                    print(f"You borrowed {book} from {self.name}.")
                    return
                else:
                    print(f"Sorry, {book} is out of stock in {self.name}.")
                    return
        print(f"{book_title} not found in {self.name}.")

    def save_to_csv(self):
        filename = os.path.join( CSV_Folder_Path, f"{self.name}.csv")
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Author", "Copies"])
            for book, count in self.books.items():
                writer.writerow([book.title, book.author, count])




# Main program
if __name__ == "__main__":
    libraries = {}

    while True:
        print("\n--- Library System ---")
        print("1. Create Library")
        print("2. Add Book")
        print("3. Show Books")
        print("4. Borrow Book")
        print("5. Exit")

        choice = input("Select funtion: ")

        if choice == "1":
            name = input("Enter library name: ")
            #libraries[name] = Library(name)

            filename = CSV_Folder_Path + f"\\{name}.csv"

           

             # Create CSV immediately for new library
            # with open(filename,"w", newline="", encoding="utf-8") as file:
            #     writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Copies"])
            #     content = file.read()
            # print(f"Library '{name}' created and CSV file '{name}.csv' initialized.")

            try:
                if os.path.exists(filename):
                    raise FileExistsError(f"Library '{name}' already exists with CSV file '{filename}'.")
                else:
                    libraries[name] = Library(name)
                    with open(filename, mode="w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerow(["Title", "Author", "Copies"])
                    print(f"Library '{name}' created and CSV file '{name}.csv' initialized.")
            except FileExistsError as e:
                print(e)
        elif choice == "2":
            lib_name = input("Enter library name: ")
            if lib_name in libraries:
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                count = int(input("Enter number of copies: "))
                book = Book(title, author)
                libraries[lib_name].add_book(book, count)
            else:
                print("Library not found.")

        elif choice == "3":
            lib_name = input("Enter library name: ")
            if lib_name in libraries:
                libraries[lib_name].show_books()
            else:
                print("Library not found.")

        elif choice == "4":
            lib_name = input("Enter library name: ")
            if lib_name in libraries:
                title = input("Enter book title to borrow: ")
                libraries[lib_name].borrow_book(title)
            else:
                print("Library not found.")

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


