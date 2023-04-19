
from Low_Ballers.email_gen import data_email
from Low_Ballers.exchange import exchange_main
from Low_Ballers.sears import get_price as get_price_sears
from Low_Ballers.target import get_price as get_price_target
from Low_Ballers.walmart import get_price as get_price_walmart

product_price = 0
user_input = ''
url = ''

def intro():

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
    print("Press 'Y' to start, 'M' for more info, 'A' for about us or 'Q' to Quit")
    print("https://www.aafes.com/exchange-stores/price-match/, Visit AAFES Price Match Policy")
    user_input = input(">")
    if user_input.lower() == "y":
        prompt_for_input()
    if user_input.lower() == "m":
        more_info()
    if user_input.lower() == "a":
        aboutus()
    else:
        user_input.lower() == 'q'
        quit()
        breakpoint()




def prompt_for_input():
    global product_price
    global url
    global user_input
    print("Please enter the ShopMyExchange URl for the product you will like to search")
    print("Ex https://www.shopmyexchange.com/apple-11-in-512gb-ipad-pro-with-wi-fi-only/3437062")
    user_input = input("Enter URL Here >")
    url = user_input
    #regex validate url
    if user_input.lower() != '' and False:
        search_failed()

    else:
        print("Please enter the price of the product you have entered")
        price_input = input("Enter price of the product, ex $49.99 > $")
        try:
            price_input = float(price_input)
        except:
            search_failed()
        product_price = price_input
        search_successful()
        breakpoint()
def search_failed():
    global url
    print("We were not able to find any matches for your search, please enter a new url or")
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
    global product_price
    global user_input
    global url
    exchange_get = exchange_main(url)
    title = exchange_get['title']
    print("Please wait while we search for you......")
    print(f" Your product was {title} at the price of ${product_price}")
    print("We were able to find the following matches for the best price :")
    # if price comes back at not available , s
    sears = get_price_sears(exchange_get)
    if sears:
        sears['price'] = format_price(sears['price'])
        sears_output = f"Sears price:${sears['price']},{sears['url']}"
    if sears is None:
        sears_output = "Could not find match for Sears"
        sears = dict()
        sears['price'] = float('inf')
    target = get_price_target(exchange_get)
    if target:
        target['price'] = format_price(target['price'])
        target_output = f"Target price:${target['price']},{target['url']}"
    if target is None:
        target_output = "Could not find match for Target"
        target = dict()
        target['price'] = float('inf')
    amazon = None
    if amazon:
        amazon_output = f"Amazon price:"
    if amazon is None:
        amazon_output = "Could not find match for Amazon"
        amazon = float('inf')
    bestbuy = None
    if bestbuy:
        bestbuy_output = f"Bestbuy price:"
    if bestbuy is None:
        bestbuy_output = "Could not find match for BestBuy"
        bestbuy = float('inf')
    walmart = get_price_walmart(exchange_get)
    if walmart:
        walmart['price'] = format_price(walmart['price'])
        walmart_output = f"Walmart price:${walmart['price']}, {walmart['url']}"
    if walmart is None:
        walmart_output = " Could not find match for Walmart"
        walmart = dict()
        walmart['price'] = float('inf')
    print(bestbuy_output)
    print(sears_output)
    print(target_output)
    print(walmart_output)
    print(amazon_output)
    user_price = lowest_price(bestbuy, sears['price'], target['price'], amazon, walmart['price'], product_price)
    print(f"The best price for your search based on all the retail stores was {user_price}")
    print(f"Press 'X' to get a copy of your search results, 'Q' to quit,  'N' for new search")
    user_input = input(">")
    if user_input.lower() == "x":
        data_email()
    if user_input.lower() == "n":
        prompt_for_input()
        breakpoint()
    else:
        user_input.lower() == 'q'
        quit()



def lowest_price(a,b,c,d,e,f):


    return min(a,b,c,d,e,f)

def more_info():
    print('''Here at Low Ballers we have created a application that allows you to price
          check against competitors for the lowest price compared to the ShopMyExchange.com
          website for veterans. We appreciate everything veterans have done and this is a small token of our appreciation.
          By simply placing the url of the product page you land on within the ShopMyExchange
          website. We take the information and search for the lowest price and return you the best deal.
          After returning you the price we also allow you to save the information to your email to have the 
          ShopMyExchange website honor it. You can find details about the policy at href='https://www.aafes.com/exchange-stores/price-match/'.
          y
          Thanks for letting us serve you''')
    print("Press 'Y' to return to main menu or 'Q' to Quit")
    user_input = input('>')
    if user_input.lower() == "y":
        intro()
    if user_input.lower() == "q":
        quit()
        breakpoint()




def aboutus():
    print("aboutus")
    pass

def quit():
    print("Thank you for letting us help you get the lowest price... Low Ballers for life")
    print('''
    ___________________________________
|#######====================#######|
|#(1)*UNITED STATES OF AMERICA*(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========ONE DOLLAR===========##|
------------------------------------
    ''')
def format_price(price):
    if price[0] == '$':
        price = price[1:]
    output = ''
    for char in price:
        if char != ',':
            output += char
    return float(output)

if __name__ == "__main__":
    intro()

















