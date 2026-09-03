from Books.books import add_book, display_book
from Members.members import add_member, display_member
from Transactions.transactions import issue_book, return_book

print("LIBRARY APPLICATION")

add_book()
display_book()

add_member()
display_member()

issue_book()
return_book()