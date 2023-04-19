import pytest
from bs4 import BeautifulSoup
from Low_Ballers.walmart import get_product_page, get_price, get_search

@pytest.mark.skip('TODO')
def test_get_product_page():
    product_dict = {'model': '27GP850-B'}
    actual_soup, actual_url = get_product_page(product_dict)
    expected_url = 'https://www.walmart.com/ip/LG-27GP850-B-27-in-16-9-Ratio-2560-x-1440-Resolution-Adaptive-Sync-QHD-165-Hz-HDR-IPS-Gaming-Monitor/842633016?from=searchResults'
    assert actual_soup is not None
    assert actual_url == expected_url

@pytest.mark.skip('TODO')
def test_get_price():
    product_dict = {'model': '27GP850-B'}
    actual = get_price(product_dict)
    expected = {'price': '$426.99',
                'url': 'https://www.walmart.com/ip/LG-27GP850-B-27-in-16-9-Ratio-2560-x-1440-Resolution-Adaptive-Sync-QHD-165-Hz-HDR-IPS-Gaming-Monitor/842633016?from=searchResults'}
    assert actual == expected

def test_get_search():
    model = '27GP850-B'
    actual = get_search(model)
    assert actual is not None



