from shopping_cart.item_package.item import Item


class Cart:

    def __init__(self):
        self.__items = []
        self.__total = 0

    def add_item_in_cart(self, item):
        """This function will add item to the item list of the cart
            and will also update the total of the cart
        """
        if isinstance(item, Item) is False:
            raise ValueError('item param should be instance of Item class')
        self.__items.append(item)
        self.__total = self.__total + item.get_sub_total()

    def get_total_cart_cost(self):
        """Get the total cost of the cart"""
        return self.__total

    def get_all_items_in_cart(self):
        return self.__items
