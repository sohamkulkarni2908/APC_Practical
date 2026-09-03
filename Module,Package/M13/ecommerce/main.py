from Products.product import show_product
from Products.category import show_category

from Customers.customer import show_customer
from Customers.address import show_address

from Orders.order import place_order
from Orders.delivery import delivery

from Payments.payment import payment
from Payments.invoice import invoice

print("E-COMMERCE APPLICATION")

show_product()
show_category()

show_customer()
show_address()

place_order()
delivery()

payment()
invoice()