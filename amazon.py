import requests
from bs4 import BeautifulSoup

url ="https://www.amazon.com/s?k=QN50LS03BAFXZA"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
print('soup',soup)

price_element = soup.find('span', {'class': 'price-group'})

price = price_element.get_text()

print(price)