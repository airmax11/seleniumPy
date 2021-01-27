class Bookshelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"There are {len(self.books)} books."


class Book:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f"Book name is {self.name} and amount is {self.amount}"


book1 = Book("Harry", 100)
book2 = Book("Germiona", 20)
print(book1)
print(book2)
bookshell = Bookshelf(book1, book2)
print(bookshell.books)
print(bookshell)