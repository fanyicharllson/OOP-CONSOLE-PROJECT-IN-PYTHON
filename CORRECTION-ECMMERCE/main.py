from order import Order
from ecommerce import ECommerce
from product import Product
from customer import Customer

# Creating customers
customer1 = Customer("Paul", "C001", ["Tecno", "Laptop", "Charger"])
customer2 = Customer("Sophia", "C002", ["Clothes", "Shoes"])
customer3 = Customer("Emma", "C003", ["Headphone"])

# Creating products
product1 = Product("P001", "Tecno", 200000, 10)
product2 = Product("P002", "Laptop", 1000000, 5)
product3 = Product("P003", "Charger", 15000, 50)

# Creating e-commerce instance
ecommerce = ECommerce()

# Adding products to the database
ecommerce.add_product(product1)
ecommerce.add_product(product2)
ecommerce.add_product(product3)

# Displaying products
ecommerce.display_products()

# Ordering products
ecommerce.order_product(customer1, "Tecno")
ecommerce.order_product(customer2, "Clothes")

# Displaying customer orders
ecommerce.display_customer_orders(customer1)
ecommerce.display_customer_orders(customer2)

# Removing a product
ecommerce.remove_product("Laptop")

