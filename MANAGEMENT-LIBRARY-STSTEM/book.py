
#Book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.avaliable_status = False
    
    def __str__(self):
        print("\n\t\tBelow are book detail information...")
        return f"\nBook Title: {self.title}\nAuthor: {self.author}\nIsbn: {self.isbn}" 
    
     
     
     