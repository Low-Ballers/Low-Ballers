import pytest
from sears import get_price, get_product_page, get_html


def test_get_price():
    assert get_price


def test_get_price():
    product_dict = {'name': 'Samsung Galaxy S21', 'category': 'Electronics'}
    expected_output = {'url': 'https://www.example.com/samsung-galaxy-s21', 'price': '$799.99'}
    result = get_price(product_dict)
    assert result == expected_output


def test_get_product_page():
    product_dict = {'upc': '889349996901', 'title': 'Samsung Galaxy S21'}
    result = get_product_page(product_dict)
    assert result is not None


def test_get_html():
    url_input = 'https://www.example.com'
    result = get_html(url_input)
    assert result is not None