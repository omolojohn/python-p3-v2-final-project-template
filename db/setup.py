#db/setup.py
import sqlite3

CONN = sqlite3.connect('db/library.db')

CURSOR = CONN.cursor()

CURSOR.execute(
    """CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        quantity INTEGER,
        member_id INTEGER,
        created_at TIMESTAMP
    )  
"""
)

CURSOR.execute(
    """CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY,
        member_name TEXT,
        email TEXT,
        phone TEXT,
        created_at TIMESTAMP 
    )
   
"""
)
CONN.commit()

CURSOR.close()
CONN.close()

