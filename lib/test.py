# lib/test.py
import unittest
import sqlite3
from datetime import datetime
from models.book import Book
from models.member import Member

DB_PATH = 'db/library.db'

class TestLibraryClasses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a fresh database for testing
        cls.conn = sqlite3.connect(DB_PATH)
        cls.c = cls.conn.cursor()
        
        # Create tables
        cls.c.execute(
            """CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author TEXT,
                quantity INTEGER,
                member_id INTEGER,
                created_at TIMESTAMP
            )"""
        )

        cls.c.execute(
            """CREATE TABLE IF NOT EXISTS members (
                id INTEGER PRIMARY KEY,
                member_name TEXT,
                email TEXT,
                phone TEXT,
                created_at TIMESTAMP 
            )"""
        )

        # Insert sample data for testing
        cls.c.execute('''INSERT INTO books (title, author, quantity, member_id, created_at) 
                         VALUES (?, ?, ?, ?, ?)''', 
                      ('Book Title', 'Book Author', 10, None, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        cls.c.execute('''INSERT INTO members (member_name, email, phone, created_at) 
                         VALUES (?, ?, ?, ?)''', 
                      ('John Omolo', 'john@example.com', '123-456-7890', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        
        cls.conn.commit()

    @classmethod
    def tearDownClass(cls):
        # Clean up - delete test data
        cls.c.execute('''DELETE FROM books WHERE title=?''', ('Book Title',))
        cls.c.execute('''DELETE FROM members WHERE email=?''', ('john@example.com',))
        cls.conn.commit()

        cls.c.close()
        cls.conn.close()

    def test_book_save(self):
        book = Book('New Book', 'New Author', 5)
        book.save()

        # Retrieve the saved book from the database
        saved_book = Book.find_by_id(book.id)
        print(f"Actual book title: {saved_book.title}")
        self.assertIsNotNone(saved_book)
        self.assertEqual(saved_book.title, 'New Book')
        self.assertEqual(saved_book.author, 'New Author')
        self.assertEqual(saved_book.quantity, 5)

    def test_member_save(self):
        member = Member('Jane Omolo', 'jane@example.com', '987-654-3210')
        member.save()

        # Retrieve the saved member from the database
        saved_member = Member.find_by_id(member.id)
        print(f"Actual member name: {saved_member.member_name}")
        self.assertIsNotNone(saved_member)
        self.assertEqual(saved_member.member_name, 'Jane Omolo')
        self.assertEqual(saved_member.email, 'jane@example.com')
        self.assertEqual(saved_member.phone, '987-654-3210')

    def test_book_delete(self):
        book = Book.find_by_id(1)
        if book:
            self.assertTrue(book.delete())

        # Ensure book is deleted
        deleted_book = Book.find_by_id(1)
        print(f"Deleted book: {deleted_book}")
        self.assertIsNone(deleted_book)

    def test_member_delete(self):
        member = Member.find_by_id(1)
        if member:
            self.assertTrue(member.delete())

        # Ensure member is deleted
        deleted_member = Member.find_by_id(1)
        print("Deleted member: {deleted_member}")
        self.assertIsNone(deleted_member)

if __name__ == '__main__':
    unittest.main()
