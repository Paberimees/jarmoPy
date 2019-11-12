from tkinter import *

#Creating the root for Tkinter GUI
root = Tk()
root.title("Welcome to money")

#Creating the main frames and canvases
main = Canvas(root, width=500, height=100)
buttonsBar = Frame(root, width=500, height=100)

#Creating the elements in main
BTCPriceLabel = Label(main, text="The current BTC price is: $10006.94")
BTCPriceChangeLabel = Label(main, text="Price change in the last 24 hours: -27.31%")

loadedimage = PhotoImage(file="images/pepeClownRapey.gif")
image = Label(main, image=loadedimage)
image.image = loadedimage

#Creating the elements in buttonsBar
BTCPriceButton = Button(buttonsBar, text="Get BTC price")

#Adding the canvases to the root window
main.grid(row=0,column=0)
buttonsBar.grid(row=1, column=0)

#Adding the elements to main
BTCPriceLabel.grid(row=0, column=0)
BTCPriceChangeLabel.grid(row=1, column=0)
image.grid(row=2, column=0)

#Adding the elements to buttonsBar
BTCPriceButton.grid(row=0, column=0)

#Make the program run
root.mainloop()



