def remove_book(all_books):
    if not all_books:
        print("No books available to remove.")
        return all_books

    isbn_to_remove = input("Enter the ISBN of the book to remove: ")

    for book in all_books:
        if str(book["isbn"]) == isbn_to_remove:
            all_books.remove(book)
            print(f"Book with ISBN {isbn_to_remove} has been removed.")
            return all_books

    print("No book found with the given ISBN.")
    return all_books
