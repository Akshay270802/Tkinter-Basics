from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Python DevLab')
root.iconbitmap('images/ProfileDevLab.ico')
root.geometry("400x400")

def show():
	myLabel = Label(root, text=var.get()).pack()


var = StringVar()

c =Checkbutton(root, text="Is Black Panther your favourite Avenger? Please check the box if YES!", variable=var, onvalue="BLACK PANTHER", offvalue="IRONMAN")
c.deselect()
c.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()