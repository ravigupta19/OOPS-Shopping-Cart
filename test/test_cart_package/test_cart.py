from shopping_cart.cart_package.cart import Cart
import pytest


@pytest.fixture()
def cart():
    return Cart()


def test_cart_should_have_add_items_as_method(cart):
    assert hasattr(cart, 'add_items')


def test_cart_should_have_get_total_cart_price(cart):
    assert hasattr(cart, 'get_total_cart_price')
