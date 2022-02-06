from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Python DevLab')
root.iconbitmap('images/ProfileDevLab.ico')

def popup():
    response = messagebox.askyesno('Python DevLab', 'This is Popup Practice!')
    #Label(root, text=response).pack()
    if response == 1:
        Label(root, text="Clicked Yes").pack()
    else:
        Label(root, text="Clicked No").pack()


Button(root, text='Popup', command=popup).pack()

root.mainloop()