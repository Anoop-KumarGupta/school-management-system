import matplotlib
import matplotlib.pyplot as pl
matplotlib.use("TKAgg")
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


import openpyxl
from openpyxl import *

import os
import tkinter as tki
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

import mysql.connector
import PIL
from PIL import Image,ImageTk




'''from tkinter import *
def donothing():
    filewin=Toplevel(root)
    button=Button(filewin,text="Do nothing button")
    button.pack()

root=Tk()
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=donothing)
filemenu.add_command(label="open",command=donothing)
filemenu.add_command(label="save",command=donothing)
filemenu.add_command(label="save as",command=donothing)
filemenu.add_command(label="Close",command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)
editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label="undo",command=donothing)
editmenu.add_separator()

editmenu.add_command(label="cut",command=donothing)
editmenu.add_command(label="copy",command=donothing)
editmenu.add_command(label="paste",command=donothing)
editmenu.add_command(label="delete",command=donothing)
editmenu.add_command(label="select all",command=donothing)


menubar.add_cascade(label="Edit",menu=editmenu)
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="Help index",command=donothing)
helpmenu.add_command(label="About..",command=donothing)
menubar.add_cascade(label="help",menu=helpmenu)
root.mainloop()

'''






root=Tk()
img=Image.open("logout.jpg")
img=img.resize((50,50),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(img)



mb=Menubutton(root,image=photo)
mb.pack()
mb.menu=Menu(mb,tearoff=0)
mb["menu"]=mb.menu


mb.menu.add_checkbutton(label="mayo")
mb.menu.add_checkbutton(label="Ketchup")
mb.pack()
root.mainloop()



































