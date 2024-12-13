def save_all_books(all_books):
    with open("all_books.csv", "w") as fp:
        for book in all_books:
            line = f"{book['title']}, {book['author']}, {book['isbn']}, {book['year']}, {book['price']}, {book['quantity']}\n"
            fp.write(line)

def append_book(book):
    """Appends a single book record to the file."""
    with open("all_books.csv", "a") as fp:
        line = f"{book['title']}, {book['author']}, {book['isbn']}, {book['year']}, {book['price']}, {book['quantity']}\n"
        fp.write(line)
