import pytest
from bs4 import BeautifulSoup
from Low_Ballers.target import get_product_page, check_single_product, get_price

# @pytest.mark.skip('TODO')
def test_get_price_upc():
    product = {
        "upc": "887276625447",
    }
    actual = get_price(product)
    expected = {'price': '2', 'url': 'https://www.target.com/p/samsung-50-34-the-frame-smart-4k-uhd-tv-charcoal-black-qn50ls03b/-/A-87435751#lnk=sametab'}

    assert actual['price']
    assert actual['url'] == expected['url']

# @pytest.mark.skip('TODO')
def test_get_price_model():
    product = {
        "model": "887276625447",
    }
    actual = get_price(product)
    expected = {'price': '$1,299.99', 'url': 'https://www.target.com/p/samsung-50-34-the-frame-smart-4k-uhd-tv-charcoal-black-qn50ls03b/-/A-87435751#lnk=sametab'}

    assert actual['price']
    assert actual['url'] == expected['url']

# @pytest.mark.skip('TODO')
def test_get_price_title():
    product = {
        "title": "887276625447",
    }
    actual = get_price(product)
    expected = {'price': '$1,299.99', 'url': 'https://www.target.com/p/samsung-50-34-the-frame-smart-4k-uhd-tv-charcoal-black-qn50ls03b/-/A-87435751#lnk=sametab'}

    assert actual['price']
    assert actual['url'] == expected['url']

# @pytest.mark.skip('TODO')
def test_get_price_failure():
    product = {
        "title": "qrst",
    }
    actual = get_price(product)
    expected = {'price': '$1,299.99', 'url': 'https://www.target.com/p/samsung-50-34-the-frame-smart-4k-uhd-tv-charcoal-black-qn50ls03b/-/A-87435751#lnk=sametab'}

    assert actual is None

# @pytest.mark.skip('TODO')
def test_check_single_product():
    soup = None
    actual = check_single_product(soup)
    assert actual is None
