from save_all_books import save_all_books

def update_book(all_books):
    if not all_books:
        print("No books available to update.")
        return all_books

    isbn_to_update = input("Enter the ISBN of the book to update: ")

    for book in all_books:
        if str(book["isbn"]) == isbn_to_update:
            print(f"Found Book: {book}")
            print("Enter new details (leave blank to keep the current value): ")
            book["title"] = input(f"New Title (current: {book['title']}): ") or book["title"]
            book["author"] = input(f"New Author (current: {book['author']}): ") or book["author"]
            book["year"] = int(input(f"New Year (current: {book['year']}): ") or book["year"])
            book["price"] = int(input(f"New Price (current: {book['price']}): ") or book["price"])
            book["quantity"] = int(input(f"New Quantity (current: {book['quantity']}): ") or book["quantity"])
            print("Book updated successfully!")
            save_all_books(all_books)
            return all_books

    print("No book found with the given ISBN.")
    return all_books
