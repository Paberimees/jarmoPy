from tkinter import *

#Creating the root for Tkinter GUI
root = Tk()
root.title("Welcome to money")
#root.resizable(0,0) add this later, so window isnt resizeable
#root.geometry("500x225") add this !!

root.rowconfigure(0, weight=1) #containers inside fill the parent grid to the max
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

#Creating the main frames and canvases
main = Canvas(root, width=500, height=100)
buttonsBar = Canvas(root, width=500, height=100)

#Creating the elements in main
BTCPriceLabel = Label(main, text="The current BTC price is: $10006.94")
BTCPriceChangeLabel = Label(main, text="Price change in the last 24 hours: -27.31%")

loadedimage = PhotoImage(file="images/honkhonk.gif")
image = Label(root, image=loadedimage)
image.image = loadedimage

#Creating the elements in buttonsBar
BTCPriceButton = Button(buttonsBar, text="Get BTC price")

#Adding the canvases to the root window
main.grid(row=0,column=0)
buttonsBar.grid(row=1, column=0)

#Adding the elements to main
BTCPriceLabel.grid(row=0, column=0)
BTCPriceChangeLabel.grid(row=1, column=0)
#image.grid(row=0, column=1)
"""
main.rowconfigure(0, weight=1)
main.rowconfigure(1, weight=1)
#main.rowconfigure(2, weight=1)
main.columnconfigure(0, weight=1)
"""

#Adding the elements to buttonsBar
BTCPriceButton.grid(row=0, column=0)
"""
buttonsBar.rowconfigure(0, weight=1)
buttonsBar.columnconfigure(0, weight=1)
"""

#Make the program run
#root.mainloop()

image.grid(row=2,column=0)
i = 0 # honk honk
while True:
    root.update_idletasks()
    root.update()
    loadedimage = PhotoImage(file="images/honkhonk.gif", format="gif -index {}".format(i))
    image.configure(image=loadedimage)
    i = i + 1
    if i > 19:
        i = 0



