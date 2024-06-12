# lib/models/book.py
# Import statements
import sqlite3
from datetime import datetime


# Define the path to the SQLite database
DB_PATH = 'db/library.db'


# Define the Book class to represent a book in the library
class Book:
    def __init__(self, title, author, quantity, member_id=None, created_at=None, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.member_id = member_id
        self.created_at = created_at if created_at else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}')>"


    # Method to save the Book object to the database
    def save(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        if self.id:
            c.execute('''UPDATE books SET title=?, author=?, quantity=?, member_id=?, created_at=? WHERE id=?''',
                      (self.title, self.author, self.quantity, self.member_id, self.created_at, self.id))
        else:
            c.execute('''INSERT INTO books (title, author, quantity, member_id, created_at) VALUES (?, ?, ?, ?, ?)''',
                      (self.title, self.author, self.quantity, self.member_id, self.created_at))
            self.id = c.lastrowid

        conn.commit()
        conn.close()


    # Method to delete the Book object from the database
    def delete(self):
        if not self.id:
            return False
        
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute('''DELETE FROM books WHERE id=?''', (self.id,))

        conn.commit()
        conn.close()

        return True


    # Static method to retrieve all books from the database
    @staticmethod
    def get_all():
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute('''SELECT * FROM books''')
        books = c.fetchall()

        conn.close()

        return [Book(*book) for book in books]


    # Static method to find a book by its id
    @staticmethod
    def find_by_id(book_id):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute('''SELECT * FROM books WHERE id=?''', (book_id,))
        book = c.fetchone()

        conn.close()

        if book:
            return Book(*book)
        else:
            return None