import pytest
from bs4 import BeautifulSoup
from Low_Ballers.target import get_product_page, check_single_product

def test_get_product_page():
    product_dict = {'upc': '1234567890'}
    result = get_product_page(product_dict)
    assert result is not None


def test_check_single_product():
    html = """
        <div>
            <div data-test="current-price">$99.99</div>
            <a href="/product/12345">Product Name</a>
        </div>
    """
    soup = BeautifulSoup(html, 'html.parser')
    result_dict = check_single_product(soup)
    assert result_dict == {'price': '$99.99', 'url': 'https://www.target.com/product/12345'}