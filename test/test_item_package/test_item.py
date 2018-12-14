from shopping_cart.item_package.item import Item
from shopping_cart.product_package.product import Product
import pytest


@pytest.fixture()
def product():
    return Product('Dove Soap', 39)


@pytest.fixture()
def item(product):
    return Item(product, 2)


def test_item_should_have_get_product_as_a_method(item):
    assert hasattr(item, 'get_product')


def test_item_should_have_get_quantity_as_a_method(item):
    assert hasattr(item, 'get_quantity')


def test_item_constructor_should_raise_exception(product):
    obj = object()
    """This test  will raise exception if product param is not an instance of product"""
    with pytest.raises(ValueError):
        Item(obj, 9)

    """This test will raise exception if quantity is not an instance of integer"""
    with pytest.raises(ValueError):
        Item(product, 9.0)

    """This test will raise exception if quantity is less than or equal to zero"""
    with pytest.raises(Exception):
        Item(product, 0)


def test_item_should_have_get_sub_total_as_method(item):
    assert hasattr(item, 'get_sub_total')


def test_item_sub_total_should_be_78(item):
    assert item.get_sub_total() == 78


def test_item_sub_total_should_round_value_by_2_decimal():
    product = Product('Test 1', 19.499)
    item = Item(product, 9)
    assert item.get_sub_total() == 175.5


def test_item_should_have_attribute_update_quantity_of_item(item):
    assert hasattr(item, 'update_quantity_of_item')


def test_item_update_quantity_of_item(product):
    item = Item(product, 4)
    assert item.get_quantity() == 4
    assert item.get_sub_total() == 156

    """Increase the quantity of the item"""
    new_quantity = 9
    expected_sub_total = product.get_price() * 9
    item.update_quantity_of_item(new_quantity)
    assert item.get_quantity() == new_quantity
    assert item.get_sub_total() == expected_sub_total

    """Decrease the quantity of the item"""
    new_quantity = 6
    expected_sub_total = product.get_price() * new_quantity
    item.update_quantity_of_item(new_quantity)
    assert item.get_quantity() == new_quantity
    assert item.get_sub_total() == expected_sub_total
