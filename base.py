from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Python DevLab')
root.iconbitmap('images/ProfileDevLab.ico')

def open():
	global my_img
	top = Toplevel()
	top.title('My Second Window')
	top.iconbitmap('images/ProfileDevLab.ico')
	my_img = ImageTk.PhotoImage(Image.open("images/gonkillua1.png"))
	my_label = Label(top, image=my_img).pack()
	btn2 = Button(top, text="close window", command=top.destroy).pack()

btn = Button(root, text="Open Second Window", width=50 , command=open).pack()

root.mainloop()