from product import Product
from order import Order

class ECommerce:
    def __init__(self):
        self._product_database = []
        self._customer_orders_database = []

    def add_product(self, product):
        self._product_database.append(product)
        print("Product added to e-commerce database")

    def display_products(self):
        print("\nProduct List:")
        for product in self._product_database:
            print(product)

    def order_product(self, customer, product_name):
        for product in self._product_database:
            if product.name == product_name and product.stock_quantity > 0:
                product.stock_quantity -= 1
                self._customer_orders_database.append((customer, product))
                print(f"{customer.name} ordered {product.name}")
                return
        print(f"Product '{product_name}' is not available or out of stock")

    def display_customer_orders(self, customer):
        print(f"\n{customer.name}'s Order Information:")
        for order in self._customer_orders_database:
            if order[0] == customer:
                print(order[1])

    def remove_product(self, product_name):
        for product in self._product_database:
            if product.name == product_name:
                self._product_database.remove(product)
                print("Product removed from e-commerce database")
                return
        print("Product not found in e-commerce database")

