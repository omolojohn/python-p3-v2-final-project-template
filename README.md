# Phase 3 CLI+ORM Project Template

# LIBRARY SYSTEM

## Phase 3: END OF PHASE PROJECT

## Date: 12-06-2024

## By: John Omolo @omolojohn

### Introduction
This project is a Python Command-Line Interface (CLI) application that manages data using Object-Relational Mapping (ORM). The application allows users to interact with a database via a CLI, providing options to create, delete, get all, and find by id at minimum. The project emphasizes the use of Python ORM methods, proper data modeling, and user-friendly CLI interactions.

### Table of Contents
 1. Features
 2. Installation
 3. Usage
 4. Data Model
 5. CLI Options
 6. Dependencies
 7. Contributing
 8. License

### Features
 .Database interaction using Python ORM methods
 .Data model with at least two classes and one-to-many relationships
 .Property methods to add constraints to model classes
 .CRUD operations (Create, Read, Update, Delete) for each model class
 .User-friendly CLI with menus and input validation
 .Error handling with informative messages

 ### Installation

To install and run this application, follow these steps:

  1. Clone the repository: git clone https://github.com/omolojohn/python-p3-v2-final-project-template.git

  2. Ensure you have Python 3.7+ installed.

  3. Install dependencies using Pipenv: pipenv install

  4. Activate the virtual environment: pipenv shell

  5. Run the application: python cli.py

### Usage
Upon running the application, a cli menu will be displayed with various options. Navigate through the menu to perform actions such as creating, deleting, and viewing objects in the database. The CLI will remain active until the user chooses to exit.

### Data Model
The data model includes at least two model classes with a one-to-many relationship. 

### CLI Options
The CLI provides options for each class in the data model:

User Options:
 .Create User
 .Delete User
 .Display All Users
 .View User's Posts
 .Find User by ID
Post Options:
 .Create Post
 .Delete Post
 .Display All Posts
 .View Related Posts by User ID
 .Find Post by ID
General Options:
 .Exit
The CLI includes loops to keep the user in the application until they choose to exit, and it validates user input to ensure correct data handling.

### Dependencies
The dependencies are managed using Pipenv. The Pipfile contains all necessary dependencies for the project. No unneeded dependencies are included.

### Contributing
Contributions are welcome! Please follow these steps:

 1. Fork the repository
 2. Create a new branch (git checkout -b feature-branch)
 3. Make your changes
 4. Commit your changes (git commit -am 'Add new feature')
 5. Push to the branch (git push origin feature-branch)
 6. Create a new Pull Request

 ### License
 MIT License

Copyright (c) 2024 omolojohn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
