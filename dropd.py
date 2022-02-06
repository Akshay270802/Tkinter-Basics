from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Python DevLab')
root.iconbitmap('images/ProfileDevLab.ico')
root.geometry("400x400")

def show():
	myLabel = Label(root, text=clicked.get()).pack()

options = [
    "Please Select a Language",
    "Python",
    "Java",
    "C++",
    "C#",
    "JavaScript",
    "PHP",
    "Ruby",
    "Swift",
    "Go",
    "Kotlin",
]	
clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()
myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()