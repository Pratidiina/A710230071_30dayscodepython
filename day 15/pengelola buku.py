class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def find_book_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        return found_books


def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Find Book by Title")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = input("Enter year of publication: ")
            book = Book(title, author, year)
            library.add_book(book)

        elif choice == '2':
            library.display_books()

        elif choice == '3':
            title = input("Enter title to search: ")
            found_books = library.find_book_by_title(title)
            if found_books:
                print("Books found:")
                for book in found_books:
                    print(book)
            else:
                print("No books found with that title.")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
