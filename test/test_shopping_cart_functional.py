from shopping_cart.cart_package.cart import Cart
from shopping_cart.item_package.item import Item
from shopping_cart.product_package.product import Product


def test_step1():
    """first create empty cart"""
    cart = Cart()

    """Create product"""
    product = Product('Dove Soap', 39.99)

    """Add the 5 Dove soap to the cart"""
    item = Item(product, 5)
    cart.add_item_in_cart(item)

    """Test step 1 scenario"""
    excepted_quantity = 5
    excepted_cost = 199.95
    excepted_product_name = 'Dove Soap'
    excepted_product_price = 39.99
    item_in_cart = cart.get_all_items_in_cart()[0]
    assert item_in_cart.get_quantity() == excepted_quantity
    assert item_in_cart.get_product().get_name() == excepted_product_name
    assert item_in_cart.get_product().get_price() == excepted_product_price
    assert cart.get_total_cart_cost() == excepted_cost


def test_step_2():
    """first create empty cart"""
    cart = Cart()

    """Create product"""
    product = Product('Dove Soap', 39.99)

    """Add the 5 Dove soap to the cart"""
    item = Item(product, 5)
    cart.add_item_in_cart(item)

    """Test step 2 scenario"""
    cart.increase_quantity_of_item(item, 3)
    excepted_quantity = 8
    excepted_cost = 319.92
    excepted_product_name = 'Dove Soap'
    excepted_product_price = 39.99
    item_in_cart = cart.get_all_items_in_cart()[0]
    assert item_in_cart.get_quantity() == excepted_quantity
    assert item_in_cart.get_product().get_name() == excepted_product_name
    assert item_in_cart.get_product().get_price() == excepted_product_price
    assert cart.get_total_cart_cost() == excepted_cost
