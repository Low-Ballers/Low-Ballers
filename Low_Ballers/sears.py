import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

def get_price(product_dict):
    # Get html
    soup, url = get_product_page(product_dict)

    result_dict = dict()
    result_dict['url'] = url

    # Check to see if this is the final product page.  If not, return None
    if soup is None:
        return None

    # Find list of products from search results
    products = soup.find_all(attrs={"class":"pricing-sale-ui"})

    price = None

    for item in products:
        price = item.text

    result_dict['price'] = price

    return result_dict

def get_product_page(product_dict):
    if 'upc' in product_dict:
        soup, url = get_html(f"https://sears.com/search={product_dict['upc']}")
        if soup:
            products = soup.find_all('app-product-card')
            if len(products) == 0:
                return soup, url
    if 'model' in product_dict:
        soup, url = get_html(f"https://sears.com/search={product_dict['model']}")
        if soup:
            products = soup.find_all('app-product-card')
            if len(products) == 0:
                return soup, url
    if 'title' in product_dict:
        soup, url = get_html(f"https://sears.com/search={product_dict['title']}")
        if soup:
            products = soup.find_all('app-product-card')
            if len(products) == 0:
                return soup, url
    else:
        return None, None

def get_html(url_input):
    with sync_playwright() as p:
        # opens browser
        browser = p.chromium.launch(headless=False, slow_mo=3000)

        # opens page
        page = browser.new_page()

        try:
            # opens url
            page.goto(url_input)

            # closes pop-up
            page.get_by_label("close")

            # Get html
            html = page.inner_html("app-root")

        except Exception as e:
            print(e)
            return None

        # Save as bs4
        soup = BeautifulSoup(html, 'html.parser')

        # closes browser
        browser.close()

    return soup, page.url

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

    print(get_price(tv))
    # print(get_price(ninja))
    #print(get_price(nike))
