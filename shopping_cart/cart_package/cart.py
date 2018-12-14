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

    def _update_the_total_of_cart(self):
        self.__total = 0
        for item in self.__items:
            self.__total = self.__total + item.get_sub_total()

    def increase_quantity_of_item(self, item, quantity):
        if item not in self.__items:
            raise ValueError('This item doesnt belong to this cart')

        if isinstance(quantity, int) is False:
            raise TypeError('Quantity should be integer')

        if quantity <= 0:
            raise ValueError('Quantity should be greater than zero')
        new_quantity = item.get_quantity() + quantity
        item.update_quantity_of_item(new_quantity)

        """This steps will recalculate the total cart"""
        self._update_the_total_of_cart()

    def decrease_quantity_of_item(self, item, quantity):
        if item not in self.__items:
            raise ValueError('This item doesnt belong to this cart')

        if isinstance(quantity, int) is False:
            raise TypeError('Quantity should be integer')

        if quantity <= 0:
            raise ValueError('Quantity should be greater than zero')

        new_quantity = item.get_quantity() - quantity

        if new_quantity < 0:
            raise Exception(
                'Can reduce quantity of item more than its current quantity')

        if new_quantity == 0:
            self.__items.remove(item)
        else:
            item.update_quantity_of_item(new_quantity)

        """This steps will recalculate the total of cart"""
        self._update_the_total_of_cart()
