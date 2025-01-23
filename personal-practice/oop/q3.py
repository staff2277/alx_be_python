class Book:
    total_books = 0

    def __init__(self):
        Book.total_books += 1

    @classmethod   
    def display_total_books(cls):
        print(cls.total_books)


book1 = Book()
book2 = Book()

book1.display_total_books()
        