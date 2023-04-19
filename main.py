from urllib.parse import urlparse


url = "https://www.shopmyexchange.com/apple-11-in-512gb-ipad-pro-with-wi-fi-only/3437062"

def intro():
    print("Welcome to LowBallers shopping for Vets ,"
          "where we match prices for Sears, Walmart, "
          "Amazon, Target, and Best Buy to give you the best price")
    print("logo.png")
    print("Press 'Y' to start or 'Q' to Quit")
    url = "https://www.aafes.com/exchange-stores/price-match/"
    parsed_url = urlparse(url)
    hyperlink = f'<a href="{parsed_url.geturl()}">Click here for more information on the ShopMyExchangePolicy</a>'
    user_input = input(">")
    if user_input.lower() == "y":
        prompt_for_input()
    else:
        user_input.lower() == 'q'
        quit()
        breakpoint()




def prompt_for_input():
    print("Please enter Shopmyexchange URl for the product you will like to search")
    print("Ex https://www.shopmyexchange.com/apple-11-in-512gb-ipad-pro-with-wi-fi-only/3437062")
    user_input = input("Enter URL Here >")
    if user_input.lower() != url:
        search_failed()

    else:
        user_input.lower() == url
        search_successful()
        breakpoint()
def search_failed():
    global url
    print("We were not able to find any matches for your search, please enter a new url")
    print("Press Q to quit")
    user_input = input(">")
    if user_input.lower() == url:
        search_successful()
        breakpoint()
    else:
        user_input.lower() == 'q'
        quit()
        breakpoint()

# Guys coming with their code for stores
def search_successful():
    print("Please wait while we search for you......")
    print("We were able to find the following matches for the best price :")
    bestbuy = 69.99
    sears = 59.99
    target = 58.99
    print(f"Best buy price:{bestbuy}")
    print(f"Sears price:{sears}")
    print(f"Target price:{target}")
    user_price = lowest_price(bestbuy, sears, target)
    print(f"The best price for your search based on all the retail stores was {user_price}")
    print(f"Press 'X' to send a copy to my email, 'Q' to quit,  'N' for new search")
    user_input = input(">")
    if user_input.lower() == "x":
        data_email()
    if user_input.lower() == "n":
        prompt_for_input()
        breakpoint()
    else:
        user_input.lower() == 'q'
        quit()



def lowest_price(a,b,c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c



def quit():
    print("Thank you for letting us help you get the lowest price... low ballers for life")

def data_email():
    pass

if __name__ == "__main__":
    intro()
    prompt_for_input()
    search_successful()
    search_failed()
    quit()