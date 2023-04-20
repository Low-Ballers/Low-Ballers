import pytest
from Low_Ballers.sears import get_price, get_product_page, get_html

# @pytest.mark.skip('TODO')
def test_get_price_upc():
    product = {
        "upc": "887276625447",
    }
    actual = get_price(product)
    expected = {'url': 'https://www.sears.com/samsung-qn50ls03b-50-inch-class-ls03b-the-frame/p-A109307316?singlePid=true', 'price': ' $1,297.99'}

    assert actual['price']
    assert actual['url'] == expected['url']

# @pytest.mark.skip('TODO')
def test_get_price_model():
    product = {
        "model": "887276625447",
    }
    actual = get_price(product)
    expected = {'url': 'https://www.sears.com/samsung-qn50ls03b-50-inch-class-ls03b-the-frame/p-A109307316?singlePid=true', 'price': ' $1,297.99'}

    assert actual['price']
    assert actual['url'] == expected['url']

# @pytest.mark.skip('TODO')
def test_get_price_title():
    product = {
        "title": "887276625447",
    }
    actual = get_price(product)
    expected = {'url': 'https://www.sears.com/samsung-qn50ls03b-50-inch-class-ls03b-the-frame/p-A109307316?singlePid=true', 'price': ' $1,297.99'}

    assert actual['price']
    assert actual['url'] == expected['url']

# @pytest.mark.skip('TODO')
def test_get_price_failure():
    product = {
        "title": "qrst",
    }
    actual = get_price(product)

    assert actual is None
