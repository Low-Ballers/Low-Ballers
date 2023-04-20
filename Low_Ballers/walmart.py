import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')


def get_price(product_dict):
    product = get_product_page(product_dict)

    if product:
        return product
    else:
        return


def get_search(model):
    soup = get_html(f"https://www.walmart.com/search?q={model}")
    search = soup.find_all(attrs={'class': 'mb0 ph1 pa0-xl bb b--near-white w-25'})
    search_results = []
    for result in search:
        product = dict()
        link = result.find('a')
        link = link['href']
        product['url'] = f'https://www.walmart.com{link}'
        price = result.find(attrs={'data-automation-id': 'product-price'})
        price = price.div.string
        product['price'] = price
        search_results.append(product)
    return search_results


def get_product_page(product_dict):
    if 'model' in product_dict.keys():
        model = product_dict['model']
    elif 'title' in product_dict.keys():
        model = product_dict['title']
    else:
        return None
    search_results = get_search(model)
    if search_results:
        return search_results[0]
    else:
        return


def get_html(url_input):  # pragma: no cover
    proxy_params = {
        'api_key': api_key,
        'url': url_input
    }

    html = requests.get(url='https://proxy.scrapeops.io/v1/', params=proxy_params, timeout=120)
    print(html.status_code)
    print(html.url)

    soup = BeautifulSoup(html.text, 'html.parser')
    return soup


if __name__ == '__main__':  # pragma: no cover
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

    lg = {'model': '27GP850-B'}

    apple = {'model': 'MNXH3LL/A', 'title': 'Apple 11 In. 512gb Ipad Pro With Wi-fi Only '}
    # print(get_price(ninja))
    print(get_price(lg))

