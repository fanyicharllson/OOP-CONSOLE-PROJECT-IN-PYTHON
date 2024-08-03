#product class================
class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        
        #initializing protected attributes(encapsulation)
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock_quantity = stock_quantity
    
    @property
    def get_product_id(self):
        return self._product_id
    
    @property
    def get_name(self):
        return self._name
    
    @property
    def get_price(self):
        return self._price
    
    @property
    def get_stock_quantity(self):
        return self._stock_quantity    
    
    def __str__(self):
        return f"\nProduct Information:\n\n Product Name: {self._name}\n Price: {self._price},\n Product Id: {self._product_id}\n Stock Quantity: {self._stock_quantity}\n"
    
    