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

        result_dict = check_single_product(soup)

        if result_dict:
            return result_dict

    if 'model' in product_dict:
        soup = get_html(f"https://www.target.com/s?searchTerm={product_dict['model']}")

        result_dict = check_single_product(soup)

        if result_dict:
            return result_dict

    if 'title' in product_dict:
        soup = get_html(f"https://www.target.com/s?searchTerm={product_dict['title']}")

        result_dict = check_single_product(soup)

        if result_dict:
            return result_dict

    return None

def get_html(url_input): # pragma: no cover
    with sync_playwright() as p:
        # opens browser
        browser = p.chromium.launch(headless=True, slow_mo=100)

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

def check_single_product(soup):
    result_dict = dict()

    if soup:
        products = soup.find_all(attrs={"data-test": "current-price"})
        if len(products) == 1:
            result_dict['price'] = products[0].text

            products = soup.find('a', href=True)
            result_dict['url'] = 'https://www.target.com' + products['href']

            return result_dict

    else:
        return None

if __name__ == '__main__': # pragma: no cover
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

    print(get_price(tv))
    print(get_price(ninja))
    print(get_price(nike))