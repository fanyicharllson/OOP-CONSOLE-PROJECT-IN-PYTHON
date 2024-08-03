#main section================

from book import Book
from member import Member
from Library import Library

print(f"\n\t\tWELCOME TO {Library.library_name}")

# Create books
book1 = Book("Economics Book", "Ndicha", 55087)
book2 = Book("Geography Book", "Michael", 45670)
book3 = Book("History", "John Paul", 23456)

# Create members
member1 = Member("Sonia", "ictu2023001")
member2 = Member("Mike", "ictu2023002")
member3 = Member("Collins", "ictu2023003")

# Create library
library = Library()

# Add books to library
library.adding_book(book1)
library.adding_book(book2)
library.adding_book(book3)

# List books in library
library.print_book()

# Remove a book from the library
library.removing_book(book1)

# Add members to the library
library.adding_memeber(member1)
library.adding_memeber(member2)
library.adding_memeber(member3)

# Remove a member from the library
library.removing_memeber(member2)

# Borrow a book from the library
library.borrow_book(book3, member1)

# List borrowed books
library.list_borrowed_books()

# Return a book to the library
library.return_book(book3, member1)

# List books in library
library.print_book()
