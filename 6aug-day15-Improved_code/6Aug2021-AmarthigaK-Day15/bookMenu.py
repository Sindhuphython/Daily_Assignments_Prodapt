'''1. Create a menu driven programme.
Add books (book title, author, description, price, distributor name/publisher name 
View all books 
View all books in alphabetical order (sorting function)
Search a book by title (filter function)
'''
import json 
import glob
import logging
from operator import itemgetter

Books_Database = []

class books:
    def book_database(self, book_title, author, description, price, publisher_name):
        self.book_title = book_title
        self.author = author
        self.description = description 
        self.price = price
        self.publisher_name =publisher_name

B = books()

while(True):
    print("Menu Driven App for Books: ")
    print("1. Add Book details to database")
    print("2. View All Books")
    print("3. View All Books in alphabetical order")
    print("4. Search a book by title ")
    print("5. Exit ")

    selection = int(input("Enter your selection: "))

    if selection ==1:
        print("\n")
        print("Add book details to the database")

        book_title = input("Enter Book name: ")
        author = input("Enter Author name: ")
        description = input("Enter Book's description: ")
        price = int(input("Enter book price in INR: Rs."))
        publisher_name = input("Enter Publisher Name: ")

        B.book_database(book_title, author, description, price, publisher_name)

        Books = {"Book_Title":book_title,
                 "Author_Name":author,
                 "Description": description,
                 "Book_Price": price,
                 "Publisher": publisher_name
                }
    
    Books_Database.append(Books)

    #print(Books_Database)

    if selection == 2:
        #print("\n")
        print("Viewing all the book details")
        print(Books_Database)
        # logging.info("If you want to see it in file, select and view the following file: ")

        Book_list =json.dumps(Books_Database)
        
        with open('BookDatabase.json', 'w+', encoding='UTF-8') as v:
            v.write(Book_list)
      
        #Checking and Showing the file
        for i in glob.glob('Book*.json'):
            print(i)

    if selection ==3:
        print("View all book details alphabetically")
        print(sorted( Books_Database, key=lambda i:i ["Book_Title"] ))
        # print(sorted(Book_list, key =str.lower["Book_Title"]))
        #print(sorted(Book_list ["Book_Title"]))


    if selection ==4:
        print("\n")
        print("Search book by title ")
        searchBook=input("Enter a book name to search")
        print(list(filter(lambda i:i["Book_Title"]==searchBook,Books_Database)))

    if selection ==5:
        print("Exit")
        break 






