books = ["Analysis of Algorithms", "Data Structures", "CSE basics"]

books.append("Fundamentals of Python")

search = input("Enter book name to search: ")
if search in books:
    print("Book found")
else:
    print("Book not found")

books.remove("CSE basics")

print("All books:", books)
print("Total books =", len(books))