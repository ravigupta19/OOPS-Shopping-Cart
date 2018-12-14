from shopping_cart.cart_package.cart import Cart
from shopping_cart.item_package.item import Item
from shopping_cart.product_package.product import Product
import pytest


@pytest.fixture()
def product():
    return Product('Dove Soap', 19)


@pytest.fixture
def item(product):
    return Item(product, 3)


@pytest.fixture()
def cart():
    return Cart()


def test_cart_should_have_add_items_in_cart_as_method(cart):
    assert hasattr(cart, 'add_item_in_cart')


def test_cart_should_have_get_total_cart_priceas_as_a_method(cart):
    assert hasattr(cart, 'get_total_cart_cost')


def test_cart_should_have_get_all_items_in_cart_as_a_method(cart):
    assert hasattr(cart, 'get_all_items_in_cart')


def test_cart_constructor(cart):
    assert cart.get_total_cart_cost() == 0
    assert len(cart.get_all_items_in_cart()) == 0


def test_cart_add_item(cart, item):
    cart.add_item_in_cart(item)
    assert len(cart.get_all_items_in_cart()) == 1
    assert cart.get_total_cart_cost() == 57


def test_cart_add_item_should_raise_exception(cart):
    """This will raise exception if try add item from non Item instance"""
    obj = object()
    with pytest.raises(ValueError):
        cart.add_item_in_cart(obj)


def test_cart_total_cost_should_be_roundup_by_2_decimal(cart):
    product = Product('Test 1', 39.99)
    item = Item(product, 5)
    cart.add_item_in_cart(item)
    expected_no_of_items = 1
    expected_total_cost_cart = 199.95
    assert len(cart.get_all_items_in_cart()) == expected_no_of_items
    assert cart.get_total_cart_cost() == expected_total_cost_cart
