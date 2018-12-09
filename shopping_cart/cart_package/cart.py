from shopping_cart.product_package.product import Product


class Cart:

    def __init__(self):
        self.__items = []
        self.__total = 0

    def add_items_in_cart(self, item):
        """This function will add the product to the cart as item and total will recalculate for the cart"""

    def get_total_cart_price(self):
        return self.__total

