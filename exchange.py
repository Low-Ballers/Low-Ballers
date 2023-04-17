import requests
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
import re

def get_html(url_input):
    req = requests.get(url_input)
    markup = req.text # converts html request to text
    soup = BeautifulSoup(markup, 'html.parser') # converts to BeautifulSoup readible format
    return soup

def get_specs(url_input):
    '''
    Creates a dictionary of specifications of a product from shop my exchange
        Parameters:
            url_input of product from shop my exchange

        Returns:
            dict with product specifications
    '''

    # Get html
    soup = get_html(url_input)

    # Get list of all paragraphs
    div_bs4_elements = soup.find_all("div")

    # Loop: find any div with this.
    # Problem: there are divs within divs that contain this.

    div_list = []

    for div in div_bs4_elements:
        if div.find_all(attrs={"class":"sku-specs-table"}):
            div_list.append(div)

    # Find all rows
    # Look at last div only (this should be the innermost div)
    row_bs4_list = div_list[-1].find_all('tr')

    # Create dict of specs
    spec_dict = dict()

    for row in row_bs4_list:
        key = row.find("th").getText()
        value = row.find("td").getText()
        spec_dict[key] = value

    return spec_dict

def get_model_from_overview(url_input):
    '''
    Gets model number from the overview section of a product from shop my exchange
        Parameters:
            url_input of product from shop my exchange

        Returns:
            string
    '''

    model = ''

    # Get html
    soup = get_html(url_input)

    elements = []

    # Get list of all paragraphs
    for elem in soup(text=re.compile(r".*Style:.*")):
        elements.append(elem)


    string_output = elements[0]
    list_output = string_output.split()
    string_output = list_output[-1]

    string_output = re.compile(r"[^\w\s]").sub("",string_output)

    print(string_output)

    return model

if __name__ == "__main__":
    url = 'https://www.shopmyexchange.com/samsung-50-in-qled-frame-4k-smart-tv-class-ls03b-qn50ls03bafxza/3182106'
    url = 'https://www.shopmyexchange.com/ninja-professional-plus-blender-with-auto-iq/2392119'
    url = 'https://www.shopmyexchange.com/nike-men-s-revolution-6-running-shoes/2724994'

    print(get_specs(url))
    print(get_model_from_overview(url))
