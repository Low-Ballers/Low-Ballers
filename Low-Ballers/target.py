import requests
from bs4 import BeautifulSoup
import re
import time
from playwright.sync_api import sync_playwright


def get_price(product_dict):
    price = get_product_page(product_dict)
    return price

def get_product_page(product_dict):
    if 'upc' in product_dict:
        soup = get_html(f"https://www.target.com/s?searchTerm={product_dict['upc']}")
        if soup:
            products = soup.find_all(attrs={"data-test": "current-price"})
            if len(products) == 1:
                return products[0].text

    if 'model' in product_dict:
        soup = get_html(f"https://www.target.com/s?searchTerm={product_dict['model']}")
        if soup:
            products = soup.find_all(attrs={"data-test": "current-price"})
            if len(products) == 1:
                return products[0].text

    if 'title' in product_dict:
        soup = get_html(f"https://www.target.com/s?searchTerm={product_dict['title']}")
        if soup:
            products = soup.find_all(attrs={"data-test": "current-price"})
            if len(products) == 1:
                return products[0].text

    else:
        return None

def get_html(url_input):
    with sync_playwright() as p:
        # opens browser
        browser = p.chromium.launch(headless=False, slow_mo=100)

        # opens page
        page = browser.new_page()

        try:
            # opens url
            page.goto(url_input)
            time.sleep(10)

            # Get html
            html = page.inner_html('section')

        except:
            return None

        # Save as bs4
        soup = BeautifulSoup(html, 'html.parser')

        # closes browser
        browser.close()

    return soup

if __name__ == '__main__':
    tv = {
        "upc": "887276625447",
        "model": "QN50LS03BAFXZA",
        "title": "Samsung 50 In. Qled Frame 4k Smart Tv Class Ls03b Qn50ls03bafxza"
    }

    ninja = {
        "model": "BN701",
        "title": "Ninja Professional Plus Blender With Auto-iq"
    }

    nike = {
        "model": "DC3728005",
        "title": "Nike Men's Revolution 6 Running Shoes",
        "brand": "Nike"
    }

    # print(get_price(tv))
    # print(get_price(ninja))
    print(get_price(nike))