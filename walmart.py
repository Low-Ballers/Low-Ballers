import requests
from bs4 import BeautifulSoup

def get_price(product_dict):
    # Get html
    soup = get_search(product_dict)

    # Check to see if this is the final product page.  If not, return None
    if soup is None:
        return None

    # Find list of products from search results
    products = soup.find_all(attrs={"itemprop":"price"})

    price = None

    for item in products:
        price = item.text

    return price

def get_search(product_dict):
    search_dict = dict()
    if 'upc' in product_dict:
        soup = get_html(f"https://www.walmart.com/search={product_dict['upc']}")


    elif 'model' in product_dict:
        soup = get_html(f"https://www.walmart.com/search={product_dict['model']}")
        products = soup.find_all('app-product-card')
        if len(products) == 0:
            return soup
    elif 'title' in product_dict:
        soup = get_html(f"https://www.walmart.com/search={product_dict['title']}")
        products = soup.find_all('app-product-card')
        if len(products) == 0:
            return soup
    else:
        return None

def get_html(url_input):
    proxy_params = {
        'api_key': 'e9da997b-22c7-4b84-be1b-81e9dfce44d1',
        'url': url_input
    }

    html = requests.get(url='https://proxy.scrapeops.io/v1/', params=proxy_params)
    soup = BeautifulSoup(html.text, 'html.parser')
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

    # print(get_price(ninja))
    print(get_price(tv))
