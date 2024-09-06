import sqlite3

CONN = sqlite3.connect('db/library.db')

CURSOR = CONN.cursor()

# Enable foreign key support in SQLite
CURSOR.execute("PRAGMA foreign_keys = ON")

# Create the 'members' table first
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

# Create the 'books' table with a foreign key constraint on 'member_id'
CURSOR.execute(
    """CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        quantity INTEGER,
        member_id INTEGER,
        created_at TIMESTAMP,
        FOREIGN KEY (member_id) REFERENCES members(id)  -- Foreign key constraint
    )  
    """
)

CONN.commit()

CURSOR.close()
CONN.close()
