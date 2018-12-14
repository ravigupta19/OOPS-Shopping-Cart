class Product:

    def __init__(self, name, price):
        self.__name = None
        self.__price = 0
        self._set_name(name)
        self._set_price(price)

    def _set_name(self, name):
        if len(name.strip()) == 0:
            raise ValueError('Product should not be null')
        self.__name = name

    def _set_price(self, price):
        price = float(price)
        if price <= 0:
            raise ValueError('Price of the product should be greater than zero')
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price
