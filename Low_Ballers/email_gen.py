from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# create a root window
def data_email(amazon, bestbuy, sears, target, walmart, exchange):



    message = f'''
    
    Thank you for using Low_Ballers application.
    Your product was {exchange} .
    
    The results you requested are as followed:
    
    {amazon}
    
    {bestbuy}
    
    {sears}
    
    {target}
    
    {walmart}
    
    {exchange}

    The ShopMyExchange policy can be found here, 
    https://www.aafes.com/exchange-stores/price-match/.
    
    Please copy this over to your email for safe storage'''

    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    root.title("Low Ballers")
    root.geometry("1200x600+300+300")
    ttk.Label(frm, text=message).grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    root.mainloop()



if __name__ == "__main__":
    data_email('Amazon: 39.99 , amazon.com/shop?=34r3243242',
               'Best buy: 29.99 , walmart.com/shop?=34232424234',
               'Sears: 42.99, sears.com/shop?= 34234224',
               'Target: 36.99 target.com/shop?=3243243242',
               'Walmart: price not available',
               'Exchange: $50.00 , www.exchange.com')









