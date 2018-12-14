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


def test_cart_increase_quantity_of_item(cart):
    assert hasattr(cart, 'increase_quantity_of_item')


def test_cart_decrease_quantity_of_item(cart):
    assert hasattr(cart, 'decrease_quantity_of_item')


def test_cart_should_raise_the_exception(cart, item, product):
    """Create item and should add to the cart"""
    cart.add_item_in_cart(item)

    """When the item object is not passed"""
    obj = object()
    with pytest.raises(ValueError):
        cart.increase_quantity_of_item(obj, 8)

    """When the quantity is passed as -1"""
    with pytest.raises(ValueError):
        cart.increase_quantity_of_item(item, -1)

    """When the quantity is passed as string"""
    with pytest.raises(TypeError):
        cart.increase_quantity_of_item(item, "4")

    """When the item object is not passed"""
    obj = object()
    with pytest.raises(ValueError):
        cart.decrease_quantity_of_item(obj, 8)

    """When the quantity is passed as -1"""
    with pytest.raises(ValueError):
        cart.decrease_quantity_of_item(item, -1)

    """When the quantity is passed as string"""
    with pytest.raises(TypeError):
        cart.decrease_quantity_of_item(item, "4")


def test_cart_increase_item_quantity(cart):
    """Create product"""
    product = Product('Dove Soap', 39.99)

    """create an item """
    item = Item(product, 5)
    cart.add_item_in_cart(item)

    """Initial checks"""
    assert len(cart.get_all_items_in_cart()) == 1
    cart_item = cart.get_all_items_in_cart()[0]
    assert cart_item.get_quantity() == 5
    assert cart.get_total_cart_cost() == 199.95

    """increase the item quantity by 5 """
    cart.increase_quantity_of_item(item, 3)
    assert len(cart.get_all_items_in_cart()) == 1
    cart_item = cart.get_all_items_in_cart()[0]
    assert cart_item.get_quantity() == 8
    assert cart.get_total_cart_cost() == 319.92


def test_cart_decrease_quantity_item(cart):
    """Create product"""
    product = Product('Dove Soap', 39.99)

    """create an item """
    item = Item(product, 5)
    cart.add_item_in_cart(item)

    """Initial checks"""
    assert len(cart.get_all_items_in_cart()) == 1
    cart_item = cart.get_all_items_in_cart()[0]
    assert cart_item.get_quantity() == 5
    assert cart.get_total_cart_cost() == 199.95

    """update the item quantity to zero"""
    descrease_quantity_by_3 = 3
    cart.decrease_quantity_of_item(item, descrease_quantity_by_3)
    assert len(cart.get_all_items_in_cart()) == 1
    cart_item = cart.get_all_items_in_cart()[0]
    assert cart_item.get_quantity() == 2
    assert cart.get_total_cart_cost() == 79.98


def test_cart_decrease_quantity_item_to_zero(cart):
    """Create product"""
    product = Product('Dove Soap', 39.99)

    """create an item """
    item = Item(product, 5)
    cart.add_item_in_cart(item)

    """Initial checks"""
    assert len(cart.get_all_items_in_cart()) == 1
    cart_item = cart.get_all_items_in_cart()[0]
    assert cart_item.get_quantity() == 5
    assert cart.get_total_cart_cost() == 199.95

    """update the item quantity to zero"""
    quantity = cart.get_all_items_in_cart()[0].get_quantity()
    cart.decrease_quantity_of_item(item, quantity)
    assert len(cart.get_all_items_in_cart()) == 0
    assert cart.get_total_cart_cost() == 0
