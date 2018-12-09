from shopping_cart.product_package.product import Product
import pytest


@pytest.fixture()
def product():
    return Product('Dove Soap', 39.99)


def test_product_should_have_get_price_as_a_method(product):
    assert hasattr(product, 'get_price')


def test_product_should_have_get_name_as_a_method(product):
    assert hasattr(product, 'get_name')


def test_product_constructor_should_raise_exception():
    """This test will raise error if you pass empty string to product constructor"""
    with pytest.raises(ValueError):
        Product('  ', 89)

    """This test will raise error if you pass price of product less than 0"""
    with pytest.raises(ValueError):
        Product('Dove', -9)

    """This test will raise error if you pass price of product as a string"""
    with pytest.raises(ValueError):
        Product('Dove', 'trge')


def test_product_get_name_as_a_method(product):
    expected_name = 'Dove Soap'
    assert product.get_name() == expected_name


def test_product_get_price_as_a_method(product):
    expected_price = 39.99
    assert product.get_price() == expected_price

