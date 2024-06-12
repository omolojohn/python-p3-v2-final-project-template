# lib/cli.py
import os
import sys
import sqlite3
from datetime import datetime
from models.book import Book
from models.member import Member

DB_PATH = 'db/library.db'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    print("Welcome to the Library Management System")
    print("1. Books")
    print("2. Members")
    print("0. Exit")

def books_menu():
    clear_screen()
    print("Books Menu")
    print("1. Add a book")
    print("2. Delete a book")
    print("3. View all books")
    print("4. View related members")
    print("5. Find a book by ID")
    print("0. Back to main menu")

def members_menu():
    clear_screen()
    print("Members Menu")
    print("1. Add a member")
    print("2. Delete a member")
    print("3. View all members")
    print("4. View related books")
    print("5. Find a member by ID")
    print("0. Back to main menu")

def validate_integer_input(input_text):
    try:
        return int(input_text)
    except ValueError:
        return None

def validate_positive_integer_input(input_text):
    value = validate_integer_input(input_text)
    if value is not None and value >= 0:
        return value
    return None