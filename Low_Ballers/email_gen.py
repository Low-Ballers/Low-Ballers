import tkinter as tk
from tkinter import messagebox

# create a root window
def data_email():
    root = tk.Tk()
    root.withdraw()

    # show a message box with some text
    messagebox.showinfo("ShopMyExchange Data", '''
    Thank you for using Low_Ballers application, 
    the results you requested are as followed:

    Best buy: 29.99 , walmart.com/shop?=34232424234
    Amazon: 39.99 , amazon.com/shop?=34r3243242
    Sears: 42.99, sears.com/shop?= 34234224
    Target: 36.99 target.com/shop?=3243243242
    Walmart: price not available 
    
    The ShopMyExchange policy can be found here, https://www.aafes.com/exchange-stores/price-match/.
    
    Please copy this over to your email for safe storage''')

    # run the main loop
    root.mainloop()
