from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Python DevLab')
root.iconbitmap('images/ProfileDevLab.ico')

#r = IntVar()
#r.set("2")<--- Practice with radiobutton

TOPPINGS = [
	("Pepperoni", "Pepperoni"),
	("Cheese", "Cheese"),
	("Corn", "Corn"),
	("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
	Radiobutton(root, text=text, variable=pizza, value=topping).pack(anchor=W)


def clicked(value):
	myLabel = Label(root, text=value)
	myLabel.pack()	

myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()