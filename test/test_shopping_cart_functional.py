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
    assert cart.get_subtotal_of_cart() == excepted_cost


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
    assert cart.get_subtotal_of_cart() == excepted_cost


def test_step3():
    """Create product"""
    product = Product('Dove Soap', 39.99)
    product2 = Product('Axe Deo’s', 99.99)

    """Create empty cart"""
    cart = Cart()

    """Adding first to the cart"""
    item = Item(product, 2)
    cart.add_item_in_cart(item)

    """ Adding second item to cart"""
    item2 = Item(product2, 2)
    cart.add_item_in_cart(item2)

    """Test step 3 scenario"""
    excepted_quantity_product1 = 2
    excepted_quantity_product2 = 2
    excepted_product1_name = 'Dove Soap'
    excepted_product1_price = 39.99
    excepted_product2_name = 'Axe Deo’s'
    excepted_product2_price = 99.99
    excepted_subtotal_cost = 279.96
    excepted_tax = 35.0
    excepted_total_cost = 314.96

    [cart_item_1, cart_item_2] = cart.get_all_items_in_cart()
    assert cart_item_1.get_quantity() == excepted_quantity_product1
    assert cart_item_2.get_quantity() == excepted_quantity_product2
    assert cart_item_1.get_product().get_name() == excepted_product1_name
    assert cart_item_1.get_product().get_price() == excepted_product1_price
    assert cart_item_2.get_product().get_name() == excepted_product2_name
    assert cart_item_2.get_product().get_price() == excepted_product2_price
    assert cart.get_subtotal_of_cart() == excepted_subtotal_cost
    assert cart.get_total_tax_of_cart() == excepted_tax
    assert cart.get_total_cart_cost() == excepted_total_cost
