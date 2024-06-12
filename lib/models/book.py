# lib/models/book.py
import sqlite3
from datetime import datetime

DB_PATH = 'db/library.db'

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

    @staticmethod
    def get_all():
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute('''SELECT * FROM books''')
        books = c.fetchall()

        conn.close()

        return [Book(*book) for book in books]

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