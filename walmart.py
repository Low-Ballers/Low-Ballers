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
    soup = get_html(f"https://www.walmart.com/search?q={product_dict['model']}")
    search_results = soup.find_all(attrs={'class':['mb0', 'ph1', 'pa0-xl', 'bb', 'b--near-white', 'w-25']})
    return search_results

def get_product_page(product_table):
    search_results = get_search(product_dict)
    return search_results

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
