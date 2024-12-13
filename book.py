import add_books
import view_all_books
import update_book
import remove_book
import lend_book
import return_book
import csv

all_books = []

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. Book Update")
    print("3. Book Remove")
    print("4. View All Books")
    print("5. Lend Book")
    print("6. Return Book")

    menu = input("Select any number: ")

    if menu == "0":
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        all_books = update_book.update_book(all_books)
    elif menu == "3":
        all_books = remove_book.remove_book(all_books)
    elif menu == "4":
        view_all_books.view_all_books(all_books)
    elif menu == "5":
        all_books = lend_book.lend_book(all_books)
    elif menu == "6":
        all_books = return_book.return_book(all_books)
    else:
        print("Choose a valid number")


def load_books():
    books = []
    try:
        with open("all_books.csv", "r") as fp:
            reader = csv.reader(fp)
            for row in reader:
                if row:  # Ensure row is not empty
                    books.append({
                        "title": row[0],
                        "author": row[1],
                        "isbn": int(row[2]),
                        "year": int(row[3]),
                        "price": int(row[4]),
                        "quantity": int(row[5]),
                    })
    except FileNotFoundError:
        print("No existing book records found.")
    return books

all_books = load_books()