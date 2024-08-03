#ecommerce class===========
from product import Product
from order import Order

class ECommerce(Product, Order): #Multiple inheritance
    
    def __init__(self, product_id, name, price, stock_quantity):
        super().__init__(product_id, name, price, stock_quantity)
        
        self._product_database = []
        self.__customer_orders_database = []
        
    
    def __str__(self):
        return f"{super().__str__()}"   
    
    
    
    #adding product to eccommerce database
    def adding_product(self):
        self._product_database.append(f"{self._name}")
        print("\n\tProduct added to eccommerce database")
    
        
        
    
    #displaying price and stock quantity of product
    def display_price_quantity(self):
        
        print("\n\tProduct name and price: ")
        for product_name in range(len(self._name)): 
            for price in range(len(self._price)):
                print(f"{self._name[product_name]} = {self._price[price]}\n")
                
       
    
    
    #order Product
    def order_product(self, product_name, price_product): 
        for productName in range(len(self._product_database)):
            for productname in self._product_database[productName]:
             if productname == product_name: 
                
                for price in range(len(self._price)):
                    for productPrice in self._price[price]:
                    
                     if productPrice == price_product:  
                       self.__customer_orders_database.append(productname)
                       print(f"{self._name} ordered {productname}")

                    else:
                      print("Invalid Price! Please try again!")
              
             else:
                print(f"We don't have such product!")
                
    
    #displayig customer ordered infomation
    def display_customer_order_info(self):
        print(f"{self._name} order infomation;\n")
        print("\n")
        print(f"Name: {self._name}")
        print(f"Order Id: {self._order_id}")
        print(f"Customer Id: {self.__customer_id}")
        print(f"Ammount in Total: {self._price}")
        
        print(f"Product:\n")
        for product in self.__customer_orders_database:
            print(product)
        
        
        
                    
                
    
    #removing product from eccommerce database
    def removing_product(self, prduct_name):
        for Productname in range(len(self._product_database)):
            for product in self._product_database[Productname]:
                if product == prduct_name:
                  self._product_database.remove(product) 
                  print("\n\tProduct removed from eccommerce database")
        
                else:
                  print("\n\tProduct not found in eccommerce database")

