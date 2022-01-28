from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.geometry('300x300')
root.title("DevLab")
root.iconbitmap("C:/Users/avpda/Dropbox/PC/Downloads/ProfileDevLab.ico")    

my_img = ImageTk.PhotoImage(Image.open("bot.music.png"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root,text="Exit Program", command=root.quit)
button_quit.pack()
root.mainloop()