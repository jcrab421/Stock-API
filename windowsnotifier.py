import numpy
from yahoo_fin import stock_info
from win10toast import ToastNotifier
toaster = ToastNotifier()


#stock1=Stock(Apple, AAPL)
#stock2=Stock(Tesla, TSLA)
#stock3=Stock(Nintendo, NTDOY)
#stock4=Stock(Amazon, AMZN)
#stock5=Stock(Disney, DIS)


stock_info.get_live_price('AAPL')
while True:
    price=stock_info.get_live_price('AAPL')
    print (price)
    if price <130:
        toaster.show_toast("Apple Stock", "Apple stock is below 500",
        duration=5,
        )
    if price >200:
        toaster.show_toast("Apple Stock", "Apple Stock is above 1500" ,
        duration=5,
        )
    
    if 130 <= price <= 200:
        toaster.show_toast("Apple Stock - Hold position",
        "AAPL is within holding pattern", 
        duration=3,
        )
    break
#Notifier for TSLA
stock_info.get_live_price('TSLA')
while True:
    price2=stock_info.get_live_price('TSLA')
    print (price2)
    if price2 <500:
        toaster.show_toast("Tesla Stock", "Tesla stock is below 500",
        duration=5,
        )
    if price2 >1500:
        toaster.show_toast("Tesla Stock", "Tesla Stock is above 1500" ,
        duration=5,
        )
    
    if 500 <= price2 <= 1500:
        toaster.show_toast("Tesla Stock - Hold position", "Tesla is in holding pattern" ,
        duration=5,
        )
        
    break
    
    #Notifier for Nintendo Games
while True:
    price3=stock_info.get_live_price('NTDOY')
    print (price3)
    if price3 <60:
        toaster.show_toast("Nintendo Stock", "Nintendo stock is below 60",
        duration=5,
        )
    if price3 >100:
        toaster.show_toast("Nintendo Stock", "Nintendo Stock is above 100" ,
        duration=5,
        )
    
    if 130 <= price3 <= 200:
        toaster.show_toast("Nintendo Stock - Hold position", "Nintendo is in holding pattern" ,
        duration=5,
        )
    
    break
# Notifier for Amazon
while True:
    price4=stock_info.get_live_price('AMZN')
    print (price4)
    if price4<130:
        toaster.show_toast("Amazon Stock", "Amazon stock is below 130",
        duration=5,
        )
    if price4 >200:
        toaster.show_toast("Amazon Stock", "Amazon Stock is above 200" ,
        duration=5,
        )
    
    if 130 <= price4 <= 200:
        toaster.show_toast("Amazon Stock - Hold position", "Amazon is in holding pattern" ,
        duration=5,
        )
    
    break

# Notifier for Disney
while True:
    price5=stock_info.get_live_price('DIS')
    print (price5)
    if price5<100:
        toaster.show_toast("Disney Stock", "Disney stock is below 100",
        duration=5,
        )
    if price5 >200:
        toaster.show_toast("Disney Stock", "Disney Stock is above 200" ,
        duration=5,
        )
    
    if 100 <= price5 <= 200:
        toaster.show_toast("Disney Stock - Hold position", "Disney is in holding pattern" ,
        duration=5,
        )
    
    break
