from shopping_cart.lib_package.lib import roundup


def test_roundup_to_1_decimal():
    x = 123.01247
    expected_x = 123.1
    assert roundup(x, 1) == expected_x


def test_roundup_to_2_decimal():
    x = 123.01247
    expected_x = 123.02
    assert roundup(x, 2) == expected_x
    x = 34.996
    expected_x = 35.0
    assert roundup(x, 2) == expected_x
