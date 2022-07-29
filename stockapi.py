from tkinter import mainloop
from yahoo_fin import stock_info


#Notifier for AAPL
ticker=input("Enter Apple inc. ticker symbol: ")
while True:
    price=stock_info.get_live_price(ticker)
    print (price)
    if price <130:
        print("Buy the dip?")
    if price >200:
        print ("Take profit?")
    
    if price >130:
        print("Hold position.")
    
    break

#Notifier for TSLA
ticker2=input("Enter Tesla ticker symbol: ")
while True:
    price2=stock_info.get_live_price(ticker2)
    print (price2)
    if price2 <500:
        print("Buy the dip?")
    if price2 >1500:
        print ("Take profit?")
    
    if price2 >500:
        print("Hold position.")
    
    break

#Notifier for Nintendo Games
ticker3=input("Enter Nintendo Games ticker symbol: ")
while True:
    price3=stock_info.get_live_price(ticker3)
    print (price3)
    if price3 <60:
        print("Buy the dip?")
    if price3 >100:
        print ("Take profit?")
    
    if price3 >60:
        print("Hold position.")
    
    break
# Notifier for Amazon
ticker4=input("Enter Amazon ticker symbol: ")
while True:
    price4=stock_info.get_live_price(ticker3)
    print (price4)
    if price4<1500:
        print("Buy the dip?")
    if price4 >3000:
        print ("Take profit?")
    
    if price4 >1500:
        print("Hold position.")
    
    break








    




    


