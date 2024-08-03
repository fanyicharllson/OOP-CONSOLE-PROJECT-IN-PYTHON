class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock_quantity = stock_quantity

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def stock_quantity(self):
        return self._stock_quantity

    def __str__(self):
        return f"Product Information:\nProduct Name: {self._name}\nPrice: {self._price}\nProduct Id: {self._product_id}\nStock Quantity: {self._stock_quantity}"

