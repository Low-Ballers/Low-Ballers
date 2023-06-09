from Low_Ballers.email_gen import data_email
from Low_Ballers.exchange import exchange_main
from Low_Ballers.sears import get_price as get_price_sears
from Low_Ballers.target import get_price as get_price_target
from Low_Ballers.walmart import get_price as get_price_walmart
from prettytable.colortable import ColorTable, Themes
from tqdm import tqdm
import time
import os

product_price = 0
url = ''

def intro(): # pragma: no cover
    '''
    Main Low Ballers program
    Prompts user for url and price of a product found on ShopMyExchange.com
    Displays prices for that product at 5 other competitor's websites
        Parameters:
            None

        Returns:
            None
    '''
    user_input = ''
    print("\033[32m" + '''
                                        *,*..**,.                               
                                      ...,.......*/                             
                               ,.   ...,,**///*..  .                            
                     * ,*.*,.(/.. ..,*/(((((((/.....*                           
                   ,  .      ,  ..,*/(########((/**/(                           
                       ,  / ##/#..*/#######%%%%##(((( (  #  (  /                
             ,  .  .        #%/#.*#%%% %%%%%%%% y%####. (. (, /* /, *            
            .          ,  / ,%##*#%%%####,%%%%%%%%#                             
                            (%####%%%%%%###%%(%####*  ,          .  , ..        
           /  /  /  / &&&&&&&&%###%%%%%%%%%%%%###  ,  .                         
         .% ,( ,%%&&&&&&&&&&%&&(########%#%%%###,(#*#/(#*#/.#* (. /  *  .       
              %%%%&&&&&&&&&&&&&%&######(/#((#(/  %  @  &  # ./ *, (  %  @       
        .  *(%%%%%&&&&&&&&&&&&&&%%%(#####(##(&&&&&  #  #  /  *  .               
        . /###%%%%%&&&&&&&&&&&&&&%(%/####(#*%%%%&&&(/ .*  ,  .  .               
         .(((##%%%%%%&&&&&&&&&&&&&&&&%%##..&##%%&%&&  (  %  %  (  *  .          
          /*#####%%%%%%%%&%&&&%&&&&&&&&#*.&%(&#&&&#&&&%&  #  /  ,               
          //((######(%%%%%#%%%%%&&&&&&&&&(%%%%(##%&(%(#,/  ,  *  /  *           
         /,/(((###########%#%%#%%%%%%%%%###%%####((#%#%#* ,/ .#  (              
         ////((((((#######(######%%%%%%.((########((/((((                       
        *//////((((((((((((###(######## /(((((((((///(((////                    
       .*/////////////((/(/((((((((((((**/((((((((**///////*                    
       **///////////*/////////////((/*,**////////***//**//,      
    ''')
    print('''
888                                   888888b.            888 888                           
888                                   888  "88b           888 888                           
888                                   888  .88P           888 888                           
888       .d88b.  888  888  888       8888888K.   8888b.  888 888  .d88b.  888d888 .d8888b  
888      d88""88b 888  888  888       888  "Y88b     "88b 888 888 d8P  Y8b 888P"   88K      
888      888  888 888  888  888       888    888 .d888888 888 888 88888888 888     "Y8888b. 
888      Y88..88P Y88b 888 d88P       888   d88P 888  888 888 888 Y8b.     888          X88 
88888888  "Y88P"   "Y8888888P"        8888888P"  "Y888888 888 888  "Y8888  888      88888P' 
                                                                                            
                                                                                                                                                                                   
'''
)
    print("\033[1;31:40m" + "Welcome to LowBallers shopping for Vets ,"
                            "where we match prices for Sears, Walmart, "
                            "Amazon, Target, and Best Buy to give you the best price")
    print("https://www.aafes.com/exchange-stores/price-match/, Visit AAFES Price Match Policy")
    while user_input != 'q':
        print("Press 'S' to search, 'M' for more info, 'A' for about us or 'Q' to Quit")


        user_input = input(">")
        if user_input.lower() == "s":
            os.system('cls' if os.name == 'nt' else 'clear')
            prompt_for_input()
        elif user_input.lower() == "m":
            os.system('cls' if os.name == 'nt' else 'clear')
            more_info()
        elif user_input.lower() == "a":
            os.system('cls' if os.name == 'nt' else 'clear')
            aboutus()
        elif user_input.lower() == 'q':
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()
        else:
            print('Bad selection, Try Again!')



def prompt_for_input(): # pragma: no cover
    global product_price
    global url
    print("Please enter the ShopMyExchange URl for the product you will like to search")
    print("Example URL: https://www.shopmyexchange.com/apple-11-in-512gb-ipad-pro-with-wi-fi-only/3437062")
    user_input = input("Enter URL Here >")
    os.system('cls' if os.name == 'nt' else 'clear')
    url = user_input
    # FUTURE: regex validate url
    if user_input.lower() != '' and False:
        search_failed()

    else:
        print("Please enter the price of the product you have entered")
        price_input = input("Enter price of the product, ex $49.99 > $")
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            price_input = float(price_input)
        except:
            search_failed()
        product_price = price_input
        search_successful()

def search_failed():
    global url
    print("We were not able to find any matches for your search")


def search_successful(): # pragma: no cover
    global product_price
    global url
    exchange_get = exchange_main(url)
    title = exchange_get['title']
    exchange_message = f" Your product was {title} at the price of ${product_price}"
    print(exchange_message)
    print("We were able to find the following matches for the best price :")
    print("Please wait while we search for you......", '\n')
    items = ['Sears', 'Target', 'Amazon', 'BestBuy', 'Walmart'] # create a list of items to iterate over
    # iterate through the list of items and update the progress bar
    for item in tqdm(items):
        time.sleep(0.1)  # simulate some work being done
        # get the price for the current item
        if item == 'Sears':
            sears = get_price_sears(exchange_get)
            if sears:
                sears['price'] = format_price(sears['price'])
                sears_output = f"Sears price:${sears['price']},{sears['url']}"
            if sears is None:
                sears_output = "Could not find match for Sears"
                sears = dict()
                sears['price'] = float('inf')

        elif item == 'Target':
            target = get_price_target(exchange_get)
            if target:
                target['price'] = format_price(target['price'])
                target_output = f"Target price:${target['price']},{target['url']}"
            if target is None:
                target_output = "Could not find match for Target"
                target = dict()
                target['price'] = float('inf')

        elif item == 'Amazon':
            amazon = None
            if amazon:
                amazon_output = f"Amazon price:"
            if amazon is None:
                amazon_output = "Did not search Amazon.  APIs cost money"
                amazon = float('inf')

        elif item == 'BestBuy':
            bestbuy = None
            if bestbuy:
                bestbuy_output = f"Bestbuy price:"
            if bestbuy is None:
                bestbuy_output = "We are Low Ballers (i.e. broke ballers).  Did not try Bestbuy"
                bestbuy = float('inf')

        elif item == 'Walmart':
            walmart = get_price_walmart(exchange_get)
            if walmart:
                walmart['price'] = format_price(walmart['price'])
                walmart_output = f"Walmart price:${walmart['price']}, {walmart['url']}"
            if walmart is None:
                walmart_output = " Could not find match for Walmart"
                walmart = dict()
                walmart['price'] = float('inf')
    os.system('cls' if os.name == 'nt' else 'clear')
    print(sears_output, '\n')
    print(target_output, '\n')
    print(amazon_output, '\n')
    print(bestbuy_output, '\n')
    print(walmart_output, '\n')

    user_price = lowest_price(bestbuy, sears['price'], target['price'], amazon, walmart['price'], product_price)
    print(f"The best price for your search based on all the retail stores was ${user_price}", '\n')
    print(f"Do you want your search results? (Y)es or (N)o?")
    user_input = input(">")
    if user_input.lower() == "y":
        data_email(amazon_output, bestbuy_output, sears_output, target_output, walmart_output, exchange_message)
    os.system('cls' if os.name == 'nt' else 'clear')

def lowest_price(a,b,c,d,e,f):
    return min(a,b,c,d,e,f)


def more_info(): # pragma: no cover
    print('''
    
Here at Low Ballers we have created a application that allows you to price
check against competitors for the lowest price compared to the ShopMyExchange.com
website for veterans. We appreciate everything veterans have done and this is a small token of our appreciation.
By simply placing the url of the product page you land on within the ShopMyExchange
website. We take the information and search for the lowest price and return you the best deal.
After returning you the price we also allow you to save the information to your email to have the 
ShopMyExchange website honor it. You can find details about the policy at https://www.aafes.com/exchange-stores/price-match/

Thanks for letting us serve you
''')


def aboutus(): # pragma: no cover
    x = ColorTable(theme=Themes.OCEAN)

    x.field_names = ["Low Ballers", "Github", "LinkedIn", "Portfolio"]
    x.add_row(["Sheldon Pierce", 'https://github.com/Sheldon-Pierce', 'https://www.linkedin.com/in/sheldon-pierce/', 'https://sheldonpierce.netlify.app/'])
    x.add_row(["Diontre Sanders", 'https://github.com/houseofpython', 'https://www.linkedin.com/in/diontresanders/', ''])
    x.add_row(["Mike Shen", 'https://github.com/mikeshen7', 'https://www.linkedin.com/in/mike-shen1/', ''])
    x.add_row(["Dominick Martin", 'https://github.com/dommcat', 'https://www.linkedin.com/in/dominickmartin/', ''])
    x.add_row(["Ethan Albers", 'https://github.com/ekalbers', 'https://www.linkedin.com/in/ethanalbers/', ''])
    print(x)

    pass


def quit(): # pragma: no cover
    print("Thank you for letting us help you get the lowest price... Low Ballers for life")
    print('''
____________________________________
|#######====================#######|
|#(1)*UNITED STATES OF AMERICA*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========ONE DOLLAR===========##|
------------------------------------
    ''')
    exit()


def format_price(price):
    output = ''
    for char in price:
        if char != ',' and char != '$' and char != ' ':
            output += char
    if '-' in output:
        lst = output.split('-')
        return float(lst[1])
    return float(output)


if __name__ == "__main__":
    intro()

















