import pytest
from bs4 import BeautifulSoup
from Low_Ballers.walmart import get_product_page, get_price, get_search


def test_get_product_page():
    product_dict = {'model': '27GP850-B'}
    actual = get_product_page(product_dict)
    expected = {
        'url': 'https://www.walmart.com/ip/LG-27GP850-B-27-in-16-9-Ratio-2560-x-1440-Resolution-Adaptive-Sync-QHD-165-Hz-HDR-IPS-Gaming-Monitor/842633016?from=searchResults',
        'price': '$426.99'
    }
    assert actual == expected


def test_get_product_page_title():
    product_dict = {'title': 'Samsung 50 In. Qled Frame 4k Smart Tv Class Ls03b Qn50ls03bafxza'}
    actual = get_product_page(product_dict)
    expected = {
        'url': 'https://www.walmart.com/ip/SAMSUNG-50-Class-LS03B-The-Frame-QLED-4K-Smart-TV-QN50LS03BAFXZA-2022/821644919?from=searchResults',
        'price': '$1,149.00'
    }
    assert actual == expected


def test_get_price():
    product_dict = {'model': '27GP850-B'}
    actual = get_price(product_dict)
    expected = {'price': '$426.99',
                'url': 'https://www.walmart.com/ip/LG-27GP850-B-27-in-16-9-Ratio-2560-x-1440-Resolution-Adaptive-Sync-QHD-165-Hz-HDR-IPS-Gaming-Monitor/842633016?from=searchResults'}
    assert actual == expected


def test_get_price_none():
    product_dict = {}
    actual = get_price(product_dict)
    expected = None
    assert actual == expected


def test_get_search():
    model = '27GP850-B'
    actual = get_search(model)
    assert actual is not None


def test_get_search_none():
    model = ''
    expected = []
    actual = get_search(model)
    assert actual == expected



