from customer import Customer

class Order(Customer):  # Inheritance
    def __init__(self, name, customer_id, customer_orders, order_id, total_amount):
        super().__init__(name, customer_id, customer_orders)
        self._order_id = order_id
        self._total_amount = total_amount

    @property
    def order_id(self):
        return self._order_id

    @property
    def total_amount(self):
        return self._total_amount

    def __str__(self):
        return f"Order Information:\nOrder Id: {self._order_id}\nCustomer: {self.name}\nTotal Amount: {self._total_amount}"

