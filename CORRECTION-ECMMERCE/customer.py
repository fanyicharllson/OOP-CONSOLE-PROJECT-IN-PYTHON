class Customer:
    def __init__(self, name, customer_id, customer_orders):
        self.__name = name
        self.__customer_id = customer_id
        self.__customer_orders = customer_orders

    @property
    def name(self):
        return self.__name

    @property
    def customer_id(self):
        return self.__customer_id

    @property
    def customer_orders(self):
        return self.__customer_orders

    def __str__(self):
        return f"Customer Details:\nCustomer Name: {self.__name}\nCustomer Id: {self.__customer_id}\nCustomer Orders: {self.__customer_orders}"

        