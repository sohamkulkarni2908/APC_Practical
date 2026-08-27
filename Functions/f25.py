books = {}


def add_book(book_id, name):
    books[book_id] = {
        "name": name,
        "available": True
    }
    print("Book added successfully.")


def issue_book(book_id):
    if book_id in books:
        if books[book_id]["available"]:
            books[book_id]["available"] = False
            print("Book issued successfully.")
        else:
            print("Book is already issued.")
    else:
        print("Book not found.")


def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned successfully.")
    else:
        print("Book not found.")


def search_book(book_id):
    if book_id in books:
        print("Book Name:", books[book_id]["name"])

        if books[book_id]["available"]:
            print("Status: Available")
        else:
            print("Status: Issued")
    else:
        print("Book not found.")


def display_books():
    print("\nAvailable Books:")

    for book_id, book in books.items():
        if book["available"]:
            print(book_id, ":", book["name"])


while True:
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        name = input("Enter book name: ")
        add_book(book_id, name)

    elif choice == 2:
        book_id = int(input("Enter book ID: "))
        issue_book(book_id)

    elif choice == 3:
        book_id = int(input("Enter book ID: "))
        return_book(book_id)

    elif choice == 4:
        book_id = int(input("Enter book ID: "))
        search_book(book_id)

    elif choice == 5:
        display_books()

    elif choice == 6:
        break

    else:
        print("Invalid choice")