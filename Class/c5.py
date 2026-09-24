class Book:
    def __init__(self,book_id,title,author,price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID: ", self.book_id)
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Price: ", self.price)

b1 = Book(101,"Introduction to AIML","Dr.Sharma",500)
b2 = Book(102,"Fundamentals of Python", "Prof.Mehra",450)
b3 = Book(103,"Advanced DSA","Prof.Pandey",350)
b1.display()
print()
b2.display()
print()
b3.display()
print()