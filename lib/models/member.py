# lib/models/member.py
# Import statements
import sqlite3
from datetime import datetime

# Setting the path to the SQLite database file
DB_PATH = 'db/library.db'

# Defining the Member class to represent a library member
class Member:
    def __init__(self, member_name, email, phone, created_at=None, id=None):
        self.id = id
        self.member_name = member_name
        self.email = email
        self.phone = phone
        self.created_at = created_at if created_at else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   
    def __repr__(self):
        return f"<Member(id={self.id}, member_name='{self.member_name}', email='{self.email}')>"

    # Defining the setter for email to include validation
    @property
    def email(self):
        return self._email

    # Defining the setter for email to include validation
    @email.setter
    def email(self, value):
        if not value:
            raise ValueError("Email cannot be empty")
        self._email = value
    
    # Method to save the Member object to the database
    def save(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        if self.id:
            c.execute('''UPDATE members SET member_name=?, email=?, phone=?, created_at=? WHERE id=?''',
                      (self.member_name, self.email, self.phone, self.created_at, self.id))
        else:
            c.execute('''INSERT INTO members (member_name, email, phone, created_at) VALUES (?, ?, ?, ?)''',
                      (self.member_name, self.email, self.phone, self.created_at))
            self.id = c.lastrowid 

        conn.commit()
        conn.close()

    # Method to delete the Member object from the database
    def delete(self):
        if not self.id:
            return False
        
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute('''DELETE FROM members WHERE id=?''', (self.id,))

        conn.commit()
        conn.close()

        return True

    # Static method to retrieve all members from the database
    @staticmethod
    def get_all():
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute('''SELECT * FROM members''')
        members = c.fetchall()

        conn.close()

        return [Member(*member) for member in members]

    
    # Static method to find a member by their id
    @staticmethod
    def find_by_id(member_id):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute('''SELECT * FROM members WHERE id=?''', (member_id,))
        member = c.fetchone()

        conn.close()

        if member:
            return Member(*member)
        else:
            return None

