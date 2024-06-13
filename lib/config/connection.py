import sqlite3

# Define the path to the SQLite database
DB_PATH = 'db/library.db'

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()