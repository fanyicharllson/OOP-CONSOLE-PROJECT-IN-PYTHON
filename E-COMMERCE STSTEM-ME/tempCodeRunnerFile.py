#ecommerce class===========
from product import Product

class ECommerce(Product): #inheritance
    def __init__(self, product_id, name, price, stock_quantity):
        
        super().__init__(product_id, name, price, stock_quantity)
        self.__product_database = []
    
    def __str__(self):
        return f"Product Info: {super().__str__()}"    
        
    
    #adding product to eccommerce database
        
   
com1 = ECommerce("002", "Cloth", 1200, 10)
com1.get_name()
