
import os
from tkinter import *

from yahoo_fin import stock_info

#window for app
window=Tk()

window.title("Stock Alert Dashboard")
window.geometry('850x500')
#watchlist stocks
mywatchlist = {'Tech Stocks': 'AAPL, GOOG, NFLX, MSFT, TSLA, FB, AMZN,', 
'Utility Stocks': 'VZ, SO, T, AWK, PPL, EIX, DUK', 
'Dow Jones': 'AAPL, AMGN, AXP, BA, CAT, CRM, CSCO, CVX, DIS, DOW, GS, HD, HON, IBM, INTC, JNJ, JPM, KO, MCD, MMM, MRK, MSFT, NKE, PG, TRV, UNH, V, VZ, WBA, WMT',
'Game Stocks': 'SONY, NTDOY, GME, EA, U, NVDA, AMD, '
}

Current_stock = StringVar()

def search_watchlist():
    enterd_text=E1.get()
    output.delete(0.0, END)
    try:
        watchlist=mywatchlist[enterd_text]
    except:
        watchlist= "Watchlist does not exist"
    output.insert(END, watchlist)

def search_stocks():
        price = stock_info.get_live_price(E2.get())
        Current_stock.set(price)

def check_stocks():
    os.system('windowsnotifier.py')

#button for searching watchlist  
b2 = Button(window, font=40, relief=RAISED, text="Search Watchlist", bg="grey", fg="black",
command=search_watchlist)
b2.place(relx=.02, rely=.45, relheight=.08, relwidth=.2, )
#button for initiating stock alerts
bs = Button(window, font=40, relief=RAISED, text="Check Stocks", bg="grey", fg="black",
command=check_stocks)
bs.place(relx=.02, rely=.1, relheight=.12, relwidth=.2, )
#entry for searching watchlist
E1 = Entry(window, bd =5)
E1.place(relx=0.02, rely=.54)

#output for watchlist
output=Text(window, width=75, height=6,wrap=WORD, background="white", )

output.place(relx=.02, rely=.6, relheight=.3,relwidth=.5  )


#label for stock price search
Label(window, text="Ticker Symbol : ").place(relx=.7,rely=.1)
Label(window, text="Stock Price:").place(relx=.68, rely=.15, relheight=.05, relwidth=.15
)
#result window for stock price
result = Label(window, text="", textvariable=Current_stock,).place(relx=.8, rely=.155)
#window for inputing stock ticker symbol
E2 = Entry(window)
E2.place(relx=.8, rely=.1)
#button for stock price search
b = Button(window, text="Display Stock Price", command=search_stocks, bg='grey', fg='black')
b.place(relx=.8, rely=.03, relheight=.05, relwidth=.15, 
)

#project assignment
Label(window, text="John Crabtree \n SWE6623\n Dr. Yan Huang\n Kennesaw State University",
 font=50, bg='gold', fg='black').place(relx=.65, rely=.6, relheight=.35, relwidth=.3
)


window.mainloop()





