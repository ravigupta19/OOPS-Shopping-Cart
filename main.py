from shopping_cart.product_package.product import Product
from shopping_cart.item_package.item import Item
from shopping_cart.cart_package.cart import Cart


def main():
    try:
        print("Started")
        """Let create Dove product"""
        product = Product('Dove Soap', 39.99)

        """create second product"""
        product2 = Product('Axe Deo', 99.99)

        """Create empty Cart for the user"""
        cart = Cart()

        """Add items to the cart"""
        item = Item(product, 2)
        cart.add_item_in_cart(item)
        print("Added first item to the cart")

        """ Add second item to the cart"""
        item2 = Item(product2, 2)
        cart.add_item_in_cart(item2)
        print("Added first item to the cart")

        """Print the Bill"""
        print("===============================================")
        print("Item_no  Product_name  Quantity")

        for count, item in enumerate(cart.get_all_items_in_cart(), 1):
            print("{0:8d}   {1:12}   {2}".format(
                count, item.get_product().get_name(), item.get_quantity()))
        print("================================================")
        print("Subtotal of bill {0}".format(cart.get_subtotal_of_cart()))
        print("Sales tax on the bill {0}".format(cart.get_total_tax_of_cart()))
        print("Total bill {0}".format(cart.get_total_cart_cost()))

    except ValueError as err:
        print("Value Error : {0}".format(err))
    except TypeError as err:
        print("Type Error : {0}".format(err))
    except Exception as err:
        print("Exception : {0}".format(err))
    finally:
        print("Finished")


if __name__ == "__main__":
    print("Executing as main program")
    main()
