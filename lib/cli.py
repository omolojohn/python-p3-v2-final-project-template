# lib/cli.py
# Import statements
import os
import sys
import sqlite3
from datetime import datetime
from models.book import Book
from models.member import Member

# Define the path to the SQLite database
DB_PATH = 'db/library.db'


# Function to clear the terminal screen based on the operating system
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to display the main menu
def main_menu():
    clear_screen()
    print("Welcome to the Library Management System")
    print("1. Books")
    print("2. Members")
    print("0. Exit")


# Function to display the books menu
def books_menu():
    clear_screen()
    print("Books Menu")
    print("1. Add a book")
    print("2. Delete a book")
    print("3. View all books")
    print("4. View related members")
    print("5. Find a book by ID")
    print("0. Back to main menu")


# Function to display the members menu
def members_menu():
    clear_screen()
    print("Members Menu")
    print("1. Add a member")
    print("2. Delete a member")
    print("3. View all members")
    print("4. View related books")
    print("5. Find a member by ID")
    print("0. Back to main menu")


# Function to validate integer input
def validate_integer_input(input_text):
    try:
        return int(input_text)
    except ValueError:
        return None


# Function to validate positive integer input
def validate_positive_integer_input(input_text):
    value = validate_integer_input(input_text)
    if value is not None and value >= 0:
        return value
    return None


# Function to add a book to the library
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    quantity = validate_positive_integer_input(input("Enter the quantity of the book: "))
    if quantity is None:
        print("Invalid quantity entered")
        return

    book = Book(title, author, quantity)
    book.save()
    print("Book added successfully")


# Function to delete a book from the library
def delete_book():
    book_id = validate_positive_integer_input(input("Enter the ID of the book to delete: "))
    if book_id is None:
        print("Invalid book ID entered")
        return

    book = Book.find_by_id(book_id)
    if book:
        book.delete()
        print("Book deleted successfully")
    else:
        print("Book not found")


# Function to view all books in the library
def view_all_books():
    books = Book.get_all()
    for book in books:
        print(book)


# Function to view related members of a book
def view_related_members():
    book_id = validate_positive_integer_input(input("Enter the ID of the book to view members: "))
    if book_id is None:
        print("Invalid book ID entered")
        return

    book = Book.find_by_id(book_id)
    if book and book.member_id:
        member = Member.find_by_id(book.member_id)
        if member:
            print(f"Related member: {member}")
        else:
            print("No related member found")
    else:
        print("Book not found or no member related")


# Function to find a book by its ID
def find_book_by_id():
    book_id = validate_positive_integer_input(input("Enter the ID of the book to find: "))
    if book_id is None:
        print("Invalid book ID entered")
        return

    book = Book.find_by_id(book_id)
    if book:
        print(book)
    else:
        print("Book not found")


# Function to add a member to the library
def add_member():
    member_name = input("Enter the name of the member: ")
    email = input("Enter the email of the member: ")
    phone = input("Enter the phone number of the member: ")

    member = Member(member_name, email, phone)
    member.save()
    print("Member added successfully")


# Function to delete a member from the library
def delete_member():
    member_id = validate_positive_integer_input(input("Enter the ID of the member to delete: "))
    if member_id is None:
        print("Invalid member ID entered")
        return

    member = Member.find_by_id(member_id)
    if member:
        member.delete()
        print("Member deleted successfully")
    else:
        print("Member not found")


# Function to view all members in the library
def view_all_members():
    members = Member.get_all()
    for member in members:
        print(member)


# Function to view related books of a member
def view_related_books():
    member_id = validate_positive_integer_input(input("Enter the ID of the member to view books: "))
    if member_id is None:
        print("Invalid member ID entered")
        return

    books = Book.get_all()
    related_books = [book for book in books if book.member_id == member_id]
    if related_books:
        for book in related_books:
            print(book)
    else:
        print("No related books found")


# Function to find a member by their ID
def find_member_by_id():
    member_id = validate_positive_integer_input(input("Enter the ID of the member to find: "))
    if member_id is None:
        print("Invalid member ID entered")
        return

    member = Member.find_by_id(member_id)
    if member:
        print(member)
    else:
        print("Member not found")


# Main CLI function to handle user input and navigation
def cli():
    while True:
        main_menu()
        choice = validate_integer_input(input("Enter your choice: "))

        if choice == 0:
            break
        elif choice == 1:
            while True:
                books_menu()
                books_choice = validate_integer_input(input("Enter your choice: "))

                if books_choice == 0:
                    break
                elif books_choice == 1:
                    add_book()
                elif books_choice == 2:
                    delete_book()
                elif books_choice == 3:
                    view_all_books()
                elif books_choice == 4:
                    view_related_members()
                elif books_choice == 5:
                    find_book_by_id()
                else:
                    print("Invalid choice. Please try again.")
                    input("Press Enter to continue...")
        elif choice == 2:
            while True:
                members_menu()
                members_choice = validate_integer_input(input("Enter your choice: "))

                if members_choice == 0:
                    break
                elif members_choice == 1:
                    add_member()
                elif members_choice == 2:
                    delete_member()
                elif members_choice == 3:
                    view_all_members()
                elif members_choice == 4:
                    view_related_books()
                elif members_choice == 5:
                    find_member_by_id()
                else:
                    print("Invalid choice. Please try again.")
                    input("Press Enter to continue...")
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


# Entry point of the script
if __name__ == "__main__":
    cli()
