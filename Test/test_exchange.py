from unittest import mock

import pytest
import requests
from bs4 import BeautifulSoup
from exchange import main, get_html, get_specs, get_model_from_overview, get_title


def test_exists_main():
    assert main


def test_exists_get_html():
    assert get_html


def test_get_html():
    url_input = 'https://www.example.com'
    expected_output = mock.Mock()
    expected_output.text = '<html><body><p>Example text</p></body></html>'

    with mock.patch('requests.get') as mock_get:
        mock_get.return_value = expected_output

        from exchange import get_html
        result = get_html(url_input)

    assert result == BeautifulSoup(expected_output.text, 'html.parser')
    mock_get.assert_called_once_with(url_input)


def test_get_title():
    # Test case 1: Valid URL input
    url_input = "https://www.shopmyexchange.com/nike-men-s-revolution-6-running-shoes/2724994"
    expected_title = "Nike Men's Revolution 6 Running Shoes "
    assert get_title(url_input) == expected_title

    # # Test case 2: Invalid URL input
    # url_input = "https://www.shopmyexchange.com/non-existent-product/0000000"
    # expected_title = ""
    # assert get_title(url_input) == expected_title
    #
    # # Test case 3: Empty URL input
    # url_input = ""
    # expected_title = ""
    # assert get_title(url_input) == expected_title





@pytest.fixture
def mock_html(monkeypatch):
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




