

#Library class
class Library:
    
    library_name = "George Mike Library"
    
    def __init__(self):
       self.books = []
       self.members = []
       self.borrowed_books = []
       
    
    def adding_book(self, book):  #adding book to the library
        self.books.append(book)
        print("Book added to Library!")
    
    
    #printing book added to Library
    def print_book(self):
        print("\t\tList of book added to the library\n")
        for book in self.books:
            print(book)
            
            
    def removing_book(self, book): #remving book from library
        if book in self.books:
            self.books.remove(book)
            print("Book removed from Library!")
        
        else:
            print("Sorry, Book not found!")        
        
    
    def adding_memeber(self, memeber): #adding memeber to library
        self.members.append(memeber)
        print("Memeber added to Library!") 
        
        
    
    def removing_memeber(self, memeber): #remving memeber from library
        if memeber in self.members:
            self.members.remove(memeber)
            print("Memeber removed from Library!")
        
        else:
            print(f"Sorry, member not this {Library.library_name}")        
        
           
    
    def borrow_book(self, book, member):
        if book in self.books and book.avaliable_status:
            book.avaliable_status = False
            self.borrowed_books.append((book, member))
            self.books.remove(book)
            print(f"Book '{book.title}' borrowed by {member.name}!")
        else:
            print("Book not available or not in the library!")
            
              
    
    def return_book(self, book, member):
        borrowed_book = (book, member)
        if borrowed_book in self.borrowed_books:
            book.avaliable_status = True
            self.borrowed_books.remove(borrowed_book)
            self.books.append(book)
            print(f"Book '{book.title}' returned by {member.name}!")
        else:
            print("No record of this book being borrowed!")
    
    def list_borrowed_books(self):
        print("\t\tList of borrowed books\n")
        for book, member in self.borrowed_books:
            print(f"{book.title} borrowed by {member.name}")
        
