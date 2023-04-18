import requests
import json
from urllib.parse import urlencode
from bs4 import BeautifulSoup
# from playwright.sync_api import sync_playwright
from threading import Event

# model number for the item
# model_number = 'QN50LS03BAFXZA'


# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, slow_mo=300)
#     page = browser.new_page()
#     page.goto(f'https://www.walmart.com/cp/electronics/3944')
#
#     # def move():
#     #     page.mouse.move(30, 30)
#
#     page.reload()
#
#     anti_bot_button = page.get_by_label('Human challenge')
#     anti_bot_button.wait_for()
#     anti_bot_button.click(delay=10000)
proxy_params = {
    'api_key': 'e9da997b-22c7-4b84-be1b-81e9dfce44d1',
    'url': "https://www.amazon.com/Nintendo-Switch-Model-Legend-Zelda-Kingdom/dp/B0BZK5M9TD?ref_=Oct_d_onr_d_468642_1&pd_rd_w=IglNg&content-id=amzn1.sym.6ee521d1-d5f5-4884-afbb-3da3aec01d76&pf_rd_p=6ee521d1-d5f5-4884-afbb-3da3aec01d76&pf_rd_r=ZDTBH64VVV03HSZ0EJX1&pd_rd_wg=hai2C&pd_rd_r=6bd80a17-b2dd-4099-b3cf-6f65f0979253&pd_rd_i=B0BZK5M9TD"
}


# html = requests.get(url='https://www.sears.com/lg-oled48c2pua-lg-oled48c2p-48-inch-oled-c2pua/p-A109139761')
html = requests.get(url='https://proxy.scrapeops.io/v1/', params=proxy_params)
soup = BeautifulSoup(html.text, 'html.parser')

def find_element(element, attribute, attr_value):
    counter = 0
    for child in element.descendants:
        counter += 1
        if type(child) == type(element.html):
            if child.attrs:
                if attribute in child.attrs.keys():
                    if attr_value in child.attrs[attribute]:
                        return child.string

# print(find_element(soup, 'class', 'a-price'))
print(len(list(soup.descendants)))









