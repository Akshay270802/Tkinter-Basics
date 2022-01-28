from tkinter import *

root = Tk()
root.geometry('300x300')
def myClick():
    myLabel = Label(root, text="I'm Akshay Panchal, B.Tech Student")
    myLabel.pack()


myButton = Button(root, text="Click ME", command=myClick, bg="black", fg="white")

myButton.pack()
root.mainloop()