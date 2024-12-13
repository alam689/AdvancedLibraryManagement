from save_all_books import save_all_books

def return_book(all_books):
    if not all_books:
        print("No books available to return.")
        return all_books

    title_to_return = input("Enter the title of the book to return: ")
    borrower_name = input("Enter borrower's name: ")

    with open("lended_books.csv", "r") as fp:
        lines = fp.readlines()

    with open("lended_books.csv", "w") as fp:
        returned = False
        for line in lines:
            record = line.strip().split(", ")
            if record[0].lower() == borrower_name.lower() and record[2].lower() == title_to_return.lower():
                returned = True
            else:
                fp.write(line)

    if returned:
        for book in all_books:
            if book["title"].lower() == title_to_return.lower():
                book["quantity"] += 1
                print(f"Book '{title_to_return}' returned successfully.")
                return all_books

        print("Book returned but not found in inventory. Please check the system.")
    else:
        print("No matching lend record found.")

    #return all_books

    save_all_books(all_books)
    return all_books
