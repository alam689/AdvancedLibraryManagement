from save_all_books import save_all_books
from save_all_books import append_book


def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = int(input("Enter ISBN Number: "))
    year = int(input("Enter Publishing Year Number: "))
    price = int(input("Enter Book Price: "))
    quantity = int(input("Enter Quantity Number: "))

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
    }

    all_books.append(book)
    append_book(book)

    print("Books Added Successfully")

    return all_books