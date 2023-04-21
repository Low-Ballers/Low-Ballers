import pytest
from Low_Ballers.main import search_failed, lowest_price, format_price


def test_search_failed_not_string():
    with pytest.raises(TypeError):
        search_failed(123)

def test_search_failed_string():
    with pytest.raises(TypeError):
        search_failed(['https://example.com'])

def test_lowest_price():
    assert lowest_price(10, 20, 30, 40, 50, 60) == 10
    assert lowest_price(-10, -20, -30, -40, -50, -60) == -60
    assert lowest_price(0, 0, 0, 0, 0, 0) == 0

def test_lowest_price_with_floats():
    assert lowest_price(1.5, 2.0, 3.1, 4.7, 5.9, 6.2) == 1.5
    assert lowest_price(-1.5, -2.0, -3.1, -4.7, -5.9, -6.2) == -6.2
    assert lowest_price(0.5, 0.0, -0.5, -1.0, -1.5, -2.0) == -2.0

def test_format_price_with_comma_separator():
    price = "$2,499.99"
    assert format_price(price) == 2499.99

def test_format_price_with_range():
    price = "$1,000 - $1,500"
    assert format_price(price) == 1500.0

