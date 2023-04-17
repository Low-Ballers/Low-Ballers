import requests
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

url = "https://www.walmart.com/ip/HP-11-6-Chromebook-AMD-A4-4GB-RAM-32GB-Storage-Black-16W64UT-ABA/592161882"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0"}
html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.text, 'html.parser')

print(soup)









