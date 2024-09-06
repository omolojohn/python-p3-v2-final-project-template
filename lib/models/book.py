# Import statements
import sqlite3
from datetime import datetime

# Define the path to the SQLite database
DB_PATH = 'db/library.db'

# Define the Book class to represent a book in the library
class Book:
    all = {}

    def __init__(self, title, author, quantity, member_id=None, created_at=None, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.quantity = quantity
        self.member_id = member_id
        self.created_at = created_at if created_at else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', author='{self.author}', member_id={self.member_id})>"

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

            # catching strategy
            type(self).all[self.id] = self

        conn.commit()
        conn.close()

    # Method to map a database row to a Python object
    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])

        if book:
            book.title = row[1]
            book.author = row[2]
            book.quantity = row[3]
            book.member_id = row[4]
        else:
            # create instance
            book = cls(row[1], row[2], row[3])

            # get id
            book.id = row[0]

            cls.all[book.id] = book

        return book

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

    @classmethod
    def fetch_all(cls):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        sql = '''
            SELECT * FROM books;
        '''
        rows = c.execute(sql).fetchall()

        conn.close()

        return [cls.instance_from_db(row) for row in rows]

    # Static method to find a book by its id
    @classmethod
    def find_by_id(cls, book_id):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute('''SELECT * FROM books WHERE id=?''', (book_id,))
        book = c.fetchone()

        conn.close()

        return cls.instance_from_db(book) if book else None
