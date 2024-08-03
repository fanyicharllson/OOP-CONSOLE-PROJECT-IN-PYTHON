#customer class============

class Customer:
    
    def __init__(self, name, customer_id, costomer_order):
        self.__name = name
        self.__customer_id = customer_id
        self.__costomer_orders = costomer_order 
        
    
    @property
    def get_name(self):
        return self.__name
    
    
    @property
    def get_customer_id(self):
        return self.__customer_id
    
    
    @property
    def get_costomer_orders(self):
        return self.__costomer_orders
        
    
    def __str__(self):
        return f"Customer Details:Customer Name: {self.__name}\n Customer Id: {self.__customer_id}\n Costomer Orders: {self.__costomer_orders}" 
    
       
        

        