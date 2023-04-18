import requests
from bs4 import BeautifulSoup
# from playwright.sync_api import sync_playwright
import re

def get_price(product_dict):
    # Get html
    soup = get_product_page(product_dict)

    # Check to see if this is the final product page.  If not, return None
    if soup is None:
        return None

    # Find list of products from search results
    products = soup.find_all(attrs={"class":"pricing-sale-ui"})

    price = None

    for item in products:
        price = item.text

    return price

def get_product_page(product_dict):
    if 'upc' in product_dict:
        soup = get_html(f"https://sears.com/search={product_dict['upc']}")
        products = soup.find_all('app-product-card')
        if len(products) == 0:
            return soup
    elif 'model' in product_dict:
        soup = get_html(f"https://sears.com/search={product_dict['model']}")
        products = soup.find_all('app-product-card')
        if len(products) == 0:
            return soup
    elif 'title' in product_dict:
        soup = get_html(f"https://sears.com/search={product_dict['title']}")
        products = soup.find_all('app-product-card')
        if len(products) == 0:
            return soup
    else:
        return None

def get_html(url_input):
    req = requests.get(url_input)
    markup = req.text # converts html request to text
    soup = BeautifulSoup(markup, 'html.parser') # converts to BeautifulSoup readible format
    return soup

def get_product_info(query):
    # ********* NOT USED - saved for future reference *********
    # Get html
    soup = get_html(f"https://sears.com/search={query}")

    # Find list of products from search results
    # Using Title, gets us 13 results
    # This is a list
    products = soup.find_all('app-product-card')

    list_output = []

    # Find 'a' tags for each product
    for tag in products:
        list_output.append(tag.find('a'))

    filtered_output = []

    # Filter by text that has model number
    for item in list_output:
        model_match = False
        for tag in item:
            if "QN50LS03BAFXZA" in tag.text:
                filtered_output.append(tag)

    print(len(filtered_output))

    return

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

    print(get_price(ninja))
    #print(get_price(nike))
