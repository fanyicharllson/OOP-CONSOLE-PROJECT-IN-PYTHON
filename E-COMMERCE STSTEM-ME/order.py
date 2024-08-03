#order class==========
from customer import Customer

class Order(Customer): #inheritance
    def __init__(self, name, customer_id, customerOrder, order_id,  total_amount):
        
        super().__init__(name, customer_id, customerOrder)
        self._order_id = order_id
        self._total_amount = total_amount
        
    
    @property
    def get_order_id(self):
        return self.__order_id  
    
    
    @property
    def get_total_amount(self):
        return self._total_amount
    
    
    def __str__(self):
        return f"Ordered Infromation:\n Order Id: {self._order_id}, Customer: {self.__customer}, Total Amount: {self._total_amount}"
    
        