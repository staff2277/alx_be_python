class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
            return f"title: {self.title}|| author: {self.author}|| pages: {self.pages}"


makhab = Book("lord of the flies", "James Gunn", 195)

print(makhab)