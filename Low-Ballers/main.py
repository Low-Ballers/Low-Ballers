
from urllib.parse import urlparse


url = "https://www.shopmyexchange.com/apple-11-in-512gb-ipad-pro-with-wi-fi-only/3437062"

def intro():
    print("\033[1;31:40m" + "Welcome to LowBallers shopping for Vets ,"
          "where we match prices for Sears, Walmart, "
          "Amazon, Target, and Best Buy to give you the best price")
    print("\033[32m" + '''
                                        *,*..**,.                               
                                      ...,.......*/                             
                               ,.   ...,,**///*..  .                            
                     * ,*.*,.(/.. ..,*/(((((((/.....*                           
                   ,  .      ,  ..,*/(########((/**/(                           
                       ,  / ##/#..*/#######%%%%##(((( (  #  (  /                
             ,  .  .        #%/#.*#%%%%%%%%%%%%%%####. (. (, /* /, *            
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
    print("Press 'Y' to start, 'M' for more info, 'A' for about us or 'Q' to Quit")
    print("<a href='https://www.aafes.com/exchange-stores/price-match/'>Visit AAFES Price Match Policy</a>")
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
    print("Please wait while we search for you......")
    print("We were able to find the following matches for the best price :")
    # if price comes back at not available , s
    bestbuy = 69.99
    sears = 59.99
    target = 58.99
    amazon = 'not available'
    walmart = 45.99
    print(f"Best buy price:{bestbuy}, url")
    print(f"Sears price:{sears}, url")
    print(f"Target price:{target}, url")
    print(f"Walmart price: {walmart}, url")
    print(f"Amazon price: {amazon}, url")
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



def lowest_price(a,b,c,d,e):

    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

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
    print("Thank you for letting us help you get the lowest price... low ballers for life")
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

def data_email():
    pass

if __name__ == "__main__":
    intro()
    prompt_for_input()
    search_successful()
    search_failed()
    quit()
















