from tkinter import *
from PIL import ImageTk,Image 
window = Tk()
window.title("Welcome")
img1 = ImageTk.PhotoImage(Image.open("download.png"))
img2 = ImageTk.PhotoImage(Image.open("download1.png"))
img3 = ImageTk.PhotoImage(Image.open("download.png"))
img4 = ImageTk.PhotoImage(Image.open("download1.png"))
img5 = ImageTk.PhotoImage(Image.open("download.png"))
img6 = ImageTk.PhotoImage(Image.open("download1.png"))
#img3 = PhotoImage(file='p15-c.png')
""" lbl = Label( window, image = img1)
lbl.grid(row=0, column=0)
bttn1 = Button( window, image = img2)
bttn1.grid(row=0, column=1)
bttn2 = Button( window, image = img3)
bttn2.grid(row=0, column=2) """
stages = [img1,img2,img3,img4,img5,img6]
window.mainloop()