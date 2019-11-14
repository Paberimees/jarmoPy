from tkinter import *
from random import randint #TEMPORARY FOR TESTING PURPOSES ONLY ATM.

#Creating some important variables
BTC_price = 8643.31
USD_price = 1
EUR_price = 1.1
GBP_price = 1.28

#Creating the root for Tkinter GUI
root = Tk()
root.title("Welcome to money")
#root.resizable(0,0) add this later, so window isnt resizeable
root.geometry("500x225")
root.iconbitmap("images/mainIcon.ico")

root.rowconfigure(0, weight=1) #containers inside fill the parent grid to the max
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

#Creating some global variables
btcCalculatorOpen = False

#Creating the main frames and canvases
main = Frame(root, width=500, height=100, highlightthickness=3,highlightcolor="black", highlightbackground="black")
buttonsBar = Frame(root, width=500, height=100, background="gray")
btcCalculator = Frame(root, width=500, height=100)

#Creating the elements in main
BTCPriceLabelTextVar = StringVar()
BTCPriceLabelTextVar.set("$" + str(BTC_price)) #set to some random default value atm
BTCPriceChangeTextVar = StringVar()
BTCPriceChangeTextVar.set("-5.34%") #set to some random default value atm

BTCPriceLabelText = Label(main, text="The current BTC price is:")
BTCPriceChangeLabelText = Label(main, text="Price change (last 24 hours)")
BTCPriceLabel = Label(main, fg="green", textvariable=BTCPriceLabelTextVar)
BTCPriceChangeLabel = Label(main, fg="green", textvariable=BTCPriceChangeTextVar)

#Creating the elements in buttonsBar
BTCPriceButton = Button(buttonsBar, text="Update BTC price", command=lambda: updateBTCPrice(randint(5000,15000) + randint(0,999) / 1000))
BTCCalculatorButton = Button(buttonsBar, text="Currency Calculator", command=lambda: BTCCalculator())
testButton = Button(buttonsBar, text="Test function", command=lambda: updateBTCPrice(randint(5000,15000) + randint(0,999) / 1000))

#Creating the elements in btcCalculator
currencyFrame = LabelFrame(btcCalculator, text="Currency")

chosenCurrency = IntVar()
currencyUSDRadio = Radiobutton(currencyFrame, text="USD", variable=chosenCurrency, value=1, command=lambda: updateCurrencyNameLabel())
currencyEURRadio = Radiobutton(currencyFrame, text="EUR", variable=chosenCurrency, value=2, command=lambda: updateCurrencyNameLabel())
currencyGBPRadio = Radiobutton(currencyFrame, text="GBP", variable=chosenCurrency, value=3, command=lambda: updateCurrencyNameLabel())
chosenCurrency.set(1) #defaults to dollars

currencyFromText = StringVar()
currencyFromText.trace("w", lambda a,b,c: calculateCurrency(currencyFromText.get())) #dont know why lambda gets 3 arguments.
currencyFromNameLabel = Label(btcCalculator, text="USD")
currencyFrom = Entry(btcCalculator, textvariable=currencyFromText)
currencyToNameLabel = Label(btcCalculator, text="BTC")
currencyTo = Label(btcCalculator)

#Helper functions, necessary for functionality.
def updateBTCPrice(newPrice):
    global BTC_price #REMOVE THIS LATER THIS IS TEMPORARY
    BTC_price = newPrice #REMOVE THIS LATER THIS IS TEMPORARY
    calculateCurrency(currencyFromText.get()) #REMOVE THIS LATER THIS IS TEMPORARY
    oldPrice = float(BTCPriceLabelTextVar.get()[1:])
    #Atm it assumes you're doing it in dollars.
    BTCPriceLabelTextVar.set("$" + str(round(newPrice,2)))
    BTCPriceChangeTextVar.set(str(round((newPrice-oldPrice)/oldPrice * 100,2)) + "%") #calculates the price change %, possibly should update this from coinmarketcap instead.
    if oldPrice > newPrice:
        BTCPriceLabel.configure(fg="red")
        BTCPriceChangeLabel.configure(fg="red")
    else:
        BTCPriceLabel.configure(fg="green")
        BTCPriceChangeLabel.configure(fg="green")

def BTCCalculator():
    global btcCalculatorOpen
    if btcCalculatorOpen:
        btcCalculator.pack_forget()
    else:
        btcCalculator.pack(fill=BOTH, expand=True)
    btcCalculatorOpen = not btcCalculatorOpen

def updateCurrencyNameLabel():
    val = chosenCurrency.get()
    set = ""
    if val == 1:
        set = "USD"
    elif val == 2:
        set = "EUR"
    elif val == 3:
        set = "GBP"
    else:
        set = "ERROR!"
    currencyFromNameLabel.configure(text=set)
    calculateCurrency(currencyFromText.get()) # maybe remove this later??

def calculateCurrency(textVal):
    try:
        textVal = float(textVal)
    except:
        return #execution failed! exit out of the function!
    chosen = chosenCurrency.get()
    if chosen == 1:
        chosen = USD_price
    elif chosen == 2:
        chosen = EUR_price
    elif chosen == 3:
        chosen = GBP_price
    else:
        return #ERROR!
    textVal = round(textVal*chosen/BTC_price,9)
    currencyTo.configure(text=str(textVal) + " BTC")

def testPrint():
    print("Test print was executed. Wow, that's amazing!")

#Adding the canvases to the root window
#main.grid(row=0,column=0)
#buttonsBar.grid(row=1, column=0)
main.pack(fill=BOTH,expand=True)
buttonsBar.pack(fill=BOTH,expand=True)
#btcCalculator.pack(fill=BOTH, expand=True) #at first DO NOT pack this, because the calculator would start out open

#Adding the elements to main
BTCPriceLabelText.grid(row=0, column=0, sticky=E)
BTCPriceLabel.grid(row=0, column=1, sticky=W)
BTCPriceChangeLabelText.grid(row=0, column=2, sticky=E)
BTCPriceChangeLabel.grid(row=0, column=3, sticky=W)
main.rowconfigure(0, weight=1)
#main.rowconfigure(1, weight=1)
main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)
main.columnconfigure(2, weight=1)
main.columnconfigure(3, weight=1)

#Adding the elements to buttonsBar
BTCPriceButton.grid(row=0, column=0)
BTCCalculatorButton.grid(row=0, column=1)
testButton.grid(row=0, column=2)
buttonsBar.rowconfigure(0, weight=1)
buttonsBar.columnconfigure(0, weight=1)
buttonsBar.columnconfigure(1, weight=1)
buttonsBar.columnconfigure(2, weight=1)

#Adding the elements to btcCalculator
currencyFrame.grid(row=0, column=0, rowspan=2)
currencyFromNameLabel.grid(row=0, column=1, sticky=SE)
currencyToNameLabel.grid(row=1, column=1, sticky=NE)
currencyFrom.grid(row=0, column=2, sticky=SW, padx=(10,0))
currencyTo.grid(row=1, column=2, sticky=NW)
btcCalculator.rowconfigure(0, weight=1)
btcCalculator.rowconfigure(1, weight=2)
btcCalculator.columnconfigure(0, weight=1)
btcCalculator.columnconfigure(1, weight=1)
btcCalculator.columnconfigure(2, weight=1)
##Adding the elements to currencyFrame in btcCalculator
currencyUSDRadio.grid(row=0, column=0)
currencyEURRadio.grid(row=1, column=0)
currencyGBPRadio.grid(row=2, column=0)

#Make the program run
#root.mainloop()
while True:
    root.update_idletasks()
    root.update()




