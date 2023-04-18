import requests
from bs4 import BeautifulSoup
# from playwright.sync_api import sync_playwright

# model number for the item
model_number = 'QN50LS03BAFXZA'
# url for target search
url = f"https://www.target.com/s?searchTerm={model_number}"
# getting the response from the url
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

print(soup)

def get_product_div(url_string):
    for div in soup.find_all('div'):
        print(div.text)


if __name__ == '__main__':
    get_product_div(url)
