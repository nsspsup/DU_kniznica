
# models/book.py

class Book:
    def __init__(self, id, title, author_id, genre_id):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id

    def __repr__(self):
        return f"<Book {self.title}>"
