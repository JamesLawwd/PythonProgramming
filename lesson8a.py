# Conductors -> This is a function inside a class (__init__()),that is used to intialize attributes
#  A class contains attributes/properties/states and behaviour/methods

class Book:
    def __int__(self, author, title, price, quantity):
        self.author = author
        self.title = title
        self.price = price
        self. quantity = quantity

    def show_book(self):
        print(f'The author is {self.author},The title is {self.title}, The price{self.price} and the quantity is {self.quantity}')

book1 = Book()
book1.price = "100$"
book1.author = "James"
book1.title = "Python concept"
book1.quantity = "20"

book1.show_book()
