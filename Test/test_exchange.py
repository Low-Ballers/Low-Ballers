from unittest import mock

import pytest
import requests
from bs4 import BeautifulSoup
from Low_Ballers.exchange import exchange_main, get_html, get_specs, get_model_from_overview, get_title


def test_exists_exchange_main():
    assert exchange_main('https://www.shopmyexchange.com/nike-men-s-revolution-6-running-shoes/2724994')

def test_exchange_main_tv():
    assert exchange_main('https://www.shopmyexchange.com/samsung-50-in-qled-frame-4k-smart-tv-class-ls03b-qn50ls03bafxza/3182106')

def test_exists_get_html():
    assert get_html

def test_get_html():
    url_input = 'https://www.example.com'
    expected_output = mock.Mock()
    expected_output.text = '<html><body><p>Example text</p></body></html>'

    with mock.patch('requests.get') as mock_get:
        mock_get.return_value = expected_output

        from Low_Ballers.exchange import get_html
        result = get_html(url_input)

    assert result == BeautifulSoup(expected_output.text, 'html.parser')
    mock_get.assert_called_once_with(url_input)


def test_get_title():
    # Test case 1: Valid URL input
    url_input = "https://www.shopmyexchange.com/nike-men-s-revolution-6-running-shoes/2724994"
    expected_title = "Nike Men's Revolution 6 Running Shoes "
    assert get_title(url_input) == expected_title

def test_main_bad_url():
    # Test case 1: Valid URL input
    url_input = "https://www.shopmyexchange.com/non-existent-product/0000000"
    actual = exchange_main(url_input)
    expected = {}
    assert actual == expected


@pytest.fixture
def mock_html(monkeypatch): # pragma: no cover
    # Mocking HTML response
    html = """
        <html>
            <body>
                <div class="sku-specs-table">
                    <table>
                        <tr><th>Model</th><td>1234</td></tr>
                        <tr><th>UPC</th><td>5678</td></tr>
                        <tr><th>Color</th><td>Red</td></tr>
                    </table>
                </div>
            </body>
        </html>
    """
    monkeypatch.setattr(requests, 'get', lambda x: html)




