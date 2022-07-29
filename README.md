Stock Alert Program

This program has three main functions which are to check the price of a stock, search
a watch list for stocks, and to trigger an alert which will automatically check the price of 5 stocks
and send a message based on the price parameters. 

To run the software you will only need python, VS Code, and the python files, 
and then run the file 'gui.py' 

The libraries you will need are 
'from yahoo_fin import stock_info' 
'from win10toast import ToastNotifier'
and import 'tkinter'

To check a stock in the watchlist enter 'Game Stocks', 'Dow Jones', 'Tech Stocks', or 'Utility Stocks'
into the search box on the lower left side, then press the 'search watchlist' button
A each query will list a number of stock Ticker Symbols

The search bar on the upper right hand will return the price of a stock after entering the ticker Symbol
and pressing the 'display price' button
The stock ticker symbol must be entered. Any stock can be searched. For example 'AAPL', 'FB', 'JNJ'

Finally, the button on the left that says 'Check Stocks', when pressed, initiates a check of 5 
stocks that I own. It automatically will check the price and then return a pop up windows notification
with the parameters I have set. For example if a stock goes below the price I set it will say the 
stock is below that level. For the purpose of demonstrating I have it set to notifiy me for every stock
even if it is within my prefered range. For example, the message will say 'Hold Position', 'Apple stock
is within holding pattern'
