def display():
    f = open("books.txt", "r")
    for line in f:
        print(line.strip())
    f.close()

def search():
    book_id = input("Enter book ID: ")
    f = open("books.txt", "r")

    for line in f:
        data = line.strip().split(",")

        if data[0] == book_id:
            print("Book found:", data)

    f.close()


def issue():
    book_id = input("Enter book ID to issue: ")
    f = open("books.txt", "r")
    lines = f.readlines()
    f.close()

    f = open("books.txt", "w")
    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = "No"

        f.write(",".join(data) + "\n")

    f.close()
    print("Book issued")


def return_book():
    book_id = input("Enter book ID to return: ")
    f = open("books.txt", "r")
    lines = f.readlines()
    f.close()

    f = open("books.txt", "w")
    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = "Yes"

        f.write(",".join(data) + "\n")

    f.close()
    print("Book returned")


def available():
    f = open("books.txt", "r")
    print("Available Books:")

    for line in f:
        data = line.strip().split(",")

        if data[3] == "Yes":
            print(data[0], data[1], data[2])

    f.close()


print("All Books:")
display()
search()
available()