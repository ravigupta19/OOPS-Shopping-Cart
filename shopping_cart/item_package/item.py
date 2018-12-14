from shopping_cart.product_package.product import Product
from shopping_cart.lib_package.lib import roundup

"""This class will consist products and quantity and subtotal of the same Items"""


class Item:

    def __init__(self, product, quantity):
        self.__product = None
        self.__quantity = 0
        self.__sub_total = 0
        self._set_quantity(quantity)
        self._set_product(product)
        self._calculate_sub_total()

    def _set_product(self, product):
        if isinstance(product, Product) is False:
            raise ValueError('product should be instance of Product Class')
        self.__product = product

    def _set_quantity(self, quantity):
        if isinstance(quantity, int) is False:
            raise ValueError('Quantity should be integer')
        if quantity <= 0:
            raise Exception('Quantity should be more than 1')
        self.__quantity = quantity

    def get_product(self):
        return self.__product

    def get_quantity(self):
        return self.__quantity

    def get_sub_total(self):
        return self.__sub_total

    def _calculate_sub_total(self):
        sub_total = self.__product.get_price() * self.__quantity
        self.__sub_total = roundup(sub_total, 2)

    def update_quantity_of_item(self, quantity):
        self.__quantity = quantity
        self._calculate_sub_total()
