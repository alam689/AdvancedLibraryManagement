from datetime import datetime, timedelta
from save_all_books import save_all_books


def lend_book(all_books):
    if not all_books:
        print("No books available to lend.")
        return all_books

    title_to_lend = input("Enter the title of the book to lend: ")
    for book in all_books:
        if book["title"].lower() == title_to_lend.lower():
            if book["quantity"] > 0:
                borrower_name = input("Enter borrower's name: ")
                phone_number = input("Enter borrower's phone number: ")
                return_date = datetime.now() + timedelta(days=14)
                
                with open("lended_books.csv", "a") as fp:
                    fp.write(f"{borrower_name}, {phone_number}, {book['title']}, {return_date.strftime('%Y-%m-%d')}")
                
                book["quantity"] -= 1
                print(f"Book '{book['title']}' lent successfully. Return due date: {return_date.strftime('%Y-%m-%d')}")
                return all_books
            else:
                print("There are not enough books available to lend.")
                save_all_books(all_books)
                return all_books


    print("No book found with the given title.")
    return all_books
