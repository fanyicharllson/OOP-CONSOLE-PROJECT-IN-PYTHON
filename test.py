# class Book:
#     def __init__(self, title, author, isbn):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.avaliable_status = False
    
#     def __str__(self):
#         print("\n\t\tBelow are book detail information...")
#         return f"\nBook Title: {self.title}\nAuthor: {self.author}\nIsbn: {self.isbn}"  
     
     




# for book in range(2):
#             book_title = input("Enter title for book {}: ".format(book + 1))
#             book_author = input("Enter author for book {}: ".format(book +1))
#             book_isbn = input("Enter isbn for book {}: ".format(book +1))

# obj = Book(book_title, book_author, book_isbn) 
# print(obj)

 
#  from book import Book
# from member import Member

# def main():
    
#     print(f"\n\n\t\t\t Welcome to George Mike Library")
#     input("Press enter here to continue... ")
#     print("\n\t Select from the menu below ")
    

# def add_book_function():  #getting book from the user
#     number_of_book = input("\n\tHow many books d you want to add? ")
#     if number_of_book.isdigit():
#         number_of_book = int(number_of_book)
#         for book in range(number_of_book):
#             book_title = input("Enter title for book {}: ".format(book + 1))
#             book_author = input("Enter author for book {}: ".format(book +1))
#             book_isbn = input("Enter isbn for book {}: ".format(book +1))
        
#         #creating book class object
#         book_object = Book(book_title, book_author, book_isbn)    
            
    

# def remove_book_function(): #removing book from the library
#     pass

# def add_memeber_function():
#     pass

# def remove_memeber_function():
#     pass

# def borrow_book_function():
#     pass

# def return_book_function():
#     pass 

# def exit_library_function():
#     print("\t\t\t\tExiting...")
#     quit()
       


# dictionary = {    #dictionary for varius use choice
#           1: add_book_function,
#           2: remove_book_function,
#           3: add_memeber_function,
#           4: remove_memeber_function,
#           5: borrow_book_function,
#           6: return_book_function,
#           7: exit_library_function
#     }

# print("\n")    
# print("1) Add a book to the library")
# print("2) Remove book from the library")
# print("3) Add Memeber to the library")
# print("4) Remove Member from the library")
# print("5) Borrow book from the library")
# print("6) Return book to the library")
# print("7) Exit library")


# choice = input("Enter you choice from above: ")
# if choice.isdigit():
#         choice = int(choice)
#         action = dictionary.get(choice)
#         if action:
#             action()
        
#         else: 
#             print("\n\tInvalid choice! Please try again.")  

# else:
#     print("\n\tError! Please try again") 


fruits = ["apple", "orange"]
print(help(fruits))
             







    
         
 
           
    