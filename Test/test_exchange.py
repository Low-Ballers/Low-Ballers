import pytest
import requests
from bs4 import BeautifulSoup

from exchange import main, get_html, get_specs, get_model_from_overview, get_title


def test_exists_main():
    assert main


@pytest.mark.skip("TODO")
def test_main(httpserver):
    url_input = httpserver.url_for("/test")
    expected_output = {
        "model": "ABC123",
        "upc": "123456789012",
        "title": "Product Title ",
    }
    output_dict = main(url_input)
    assert output_dict == expected_output


def test_exists_get_html():
    assert get_html


def test_get_html():
    # Create a mock response
    class MockResponse:
        def __init__(self, text):
            self.text = text

    # Patch the requests.get method to return a mock response
    requests.get = lambda url: MockResponse("<html><head></head><body><p>Hello World!</p></body></html>")

    # Call the get_html function with the test URL
    soup = get_html("http://example.com")

    # Check that the soup object was created correctly
    assert isinstance(soup, BeautifulSoup)
    assert soup.body.p.string == "Hello World!"


def test_exists_get_specs():
    assert get_specs


def test_get_specs():
    url_input = 'https://www.shopmyexchange.com/nike-men-s-revolution-6-running-shoes/2724994'
    expected_output = {'Warmlined': 'No', 'Style Athletic Shoes': 'Running', 'Gender': 'Men', 'Shipping By Air Prohibited': 'No', 'Type Of Footwear': 'Athletic Shoes', 'Type Of Specialist Activity': 'Running', 'Style Cooking Appliances': 'Manmade Material', 'Advertised Origin': 'Imported', 'Consumer Item Height': '4.88', 'Consumer Item Width': '9.33', 'Consumer Item Length': '14.25', 'Capacity/Volume': '', 'Open/closed Upper': 'Unclassified', 'Consumer Item Weight': '2.2', 'Fastening Type': 'Lace Up', 'Brand': 'Nike', 'Width': '9.33 Inch', 'Weight': '2.2 Pounds', 'Made In America (Y/N)': 'No', 'Depth': '', 'Care Information': 'Hand Wash', 'Height': '4.88 Inch', 'Length': '14.25 Inch', 'Type Of Partially Enclosed Upper': 'Unclassified'}

    output_dict = get_specs(url_input)

    assert output_dict == expected_output


def test_exists_overview():
    assert get_model_from_overview


def test_exists_title():
    assert get_title


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