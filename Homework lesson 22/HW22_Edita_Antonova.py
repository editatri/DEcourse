import pandas as pd
import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                            'SERVER=EANTONOVA-MBL;'
                            'DATABASE=AdventureWorksDW2017;'
                            'Trusted_Connection=yes;')

connection.autocommit = True
cursor = connection.cursor()

# create Database Library
cursor.execute('''create database Library''')

cursor.execute('''use Library''')

# create table Books and populate it with values
cursor.execute('''
                    create table Books (BookID INT Primary Key
                    , Title VARCHAR(255) NOT NULL
                    , Author VARCHAR(255) NOT NULL
                    , PublishedYear INT CHECK (PublishedYear > 1800))''')

cursor.execute('''
                INSERT INTO Books
                VALUES (1, 'The Catcher in the Rye', 'J. D. Salinger''s', 1951 ),
                (2, 'The Handmaid''s Tale', 'Margaret Atwood', 1985),
                (3, 'Animal Farm', 'George Orwell', 1945)
                ''')


# create table Borrowers and populate it with values
cursor.execute('''
create table Borrowers (BorrowerID INT Primary Key
                       , Name VARCHAR(255) NOT NULL
                       , Email VARCHAR(255) UNIQUE)
''')

cursor.execute('''
                INSERT INTO Borrowers
                VALUES (376, 'Ashley Lewis', 'alewis@mail.com' ),
                (123, 'Connor Jones', 'cjones@mail.com'),
                (11, 'Mattew Thompson', 'mthompson@mail.com') ''')

# create table Loans and populate it with values
cursor.execute('''
create table Loans (LoanID INT Primary Key
                   , LoanDate DATE NOT NULL
                   , ReturnDate DATE 
                   , BookID INT
                   , BorrowerID INT
                   , CONSTRAINT FK_BookID Foreign Key (BookID) REFERENCES Books(BookID) ON DELETE CASCADE
                   , CONSTRAINT FK_BorrowerID Foreign Key (BorrowerID) REFERENCES Borrowers(BorrowerID) ON DELETE CASCADE
                   , CHECK(ReturnDate > LoanDate))
''')

cursor.execute('''
                INSERT INTO Loans
                VALUES (1, '2024-10-02', '2024-11-02', 2, 123),
                (2, '2024-09-14', '2024-10-14', 1, 376),
                (3, '2024-11-10', '2024-12-10', 3, 11) ''')
connection.close()



