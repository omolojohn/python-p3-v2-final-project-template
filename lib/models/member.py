# lib/models/member.py
import sqlite3
from datetime import datetime

DB_PATH = 'db/library.db'

class Member:
    def __init__(self, member_name, email, phone, created_at=None, id=None):
        self.id = id
        self.member_name = member_name
        self.email = email
        self.phone = phone
        self.created_at = created_at if created_at else datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        return f"<Member(id={self.id}, member_name='{self.member_name}', email='{self.email}')>"

    @staticmethod
    def get_all():
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        c.execute('''SELECT * FROM members''')
        members = c.fetchall()

        conn.close()

        return [Member(*member) for member in members]

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

