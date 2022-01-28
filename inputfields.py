from tkinter import *

root = Tk()
root.geometry('300x300')

e = Entry(root,borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name")
def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text="Click", command=myClick, bg="black", fg="white")
myButton.pack()

root.mainloop()