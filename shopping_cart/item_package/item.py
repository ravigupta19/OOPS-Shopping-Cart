from shopping_cart.product_package.product import Product


class Item:

    def __init__(self, product, quantity):
        self.__product = None
        self.__quantity = 0
        self._set_product(product)
        self._set_quantity(quantity)

    def _set_product(self, product):
        if isinstance(product, Product):
            raise TypeError('product should be instance of Product Class')
        self.__product = product

    def _set_quantity(self, quantity):
        if isinstance(quantity, int):
            raise TypeError('Quantity should be integer')
        self.__quantity = quantity

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity
