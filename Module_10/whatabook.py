import sys
import mysql.connector
from mysql.connector import errorcode
#database connection
config = {
    "user": "root",
    "password": "ChangeMe21!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
print()
# Definding reveal options
def display_books():
    db = mysql.connector.connect(**config) 
    cursor = db.cursor()
    query = "SELECT book_id, title, author, publication_date FROM book"
    cursor.execute(query)
    books = cursor.fetchall()
    print()
    print("Available Books:")
    print()
    for row in books:
        #dispyaing books
        print("Book Id: = ", row[0], )
        print("Title: = ", row[1])
        print("Author:  = ", row[2])
        print("Publication Date: = ", row[3], "\n")
       
    cursor.close()
    sys.exit()
    db.exit()
# Definding books
def show_book_info(book_id):
    db = mysql.connector.connect(**config) 
    cursor = db.cursor()
    query = "SELECT title, author, publication_date FROM book WHERE book_id = %s"
    cursor.execute(query, (book_id,))
    book_info = cursor.fetchone()
    if book_info:
        print ()
        print(f"Book: {book_info[0]}\nAuthor: {book_info[1]}\nPublication Date: {book_info[2]}")
        print()
    else:
        print("The Book is not found!.")
    cursor.close()
def main_menu():
    while True:
        print()
        print("**** Welcome to Whatabook Book****")
        print ()
        print("1. Show Available Books")
        print("2. Show Book Information")
        print("3. Exit")
        print()
        User_choice = input("Please Enter your choice: ")
        
        if User_choice == "1":
            display_books()
        elif User_choice == "2":
            book_id = int(input("Enter the book ID: "))
            show_book_info(book_id)
        elif User_choice == "3":
            print("Thanks for your time! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()