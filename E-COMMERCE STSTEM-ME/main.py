#main.py=========

from order import Order
from ecommerce import ECommerce

#creating customer inside class order(inheritance)

order1 = Order("Paul", "C001", ["Tecno", "Labtop", "Charger"], "R001", 200000)

order2 = Order("Sophia", "C002", ["Clothes", "Shoes"],"R002", 1000000)

order3 = Order("Emma", "C003", "Headphone", "R003", 500000)


#creating ecommerce instance/ products items
ecom1 = ECommerce("P001", ["Tecno", "Laptop", "Charger", "Clothes", "Shoes", "Headphone", "Food", "Oil", "Red Oil", "Cube"],[200000, 1000000, 15000, 300000, 500000, 360000, 10000, 2000000, 600000, 1000] , 10)

#adding product to database
ecom1.adding_product()

#Displaying product name  and price
ecom1.display_price_quantity()

#Ordering for a product
ecom1.order_product("Tecno", 200000)

#displaying customer order info
ecom1.display_customer_order_info() 

#removing product
ecom1.removing_product("Laptop")

  

