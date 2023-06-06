import mysql.connector
from tkinter import *
from tkinter import messagebox
db=mysql.connector.connect(host='localhost',user='root',password='program',database='school')

my_cur=db.cursor()


root=Tk()
root.title('Student Details')
root.geometry('250x300')
Label(root,text='STUDENT ENTRY FORM',font='arial 14 bold').grid(row=0,columnspan=2)
Label(root,text='').grid(row=1,column=0)
Label(root,text='Admission No.').grid(row=2,column=0)
Label(root,text='').grid(row=3,column=0)
Label(root,text='Student Name').grid(row=4,column=0)
Label(root,text='').grid(row=5,column=0)
Label(root,text='class').grid(row=6,column=0)
Label(root,text='').grid(row=7,column=0)
Label(root,text='Mobile No').grid(row=8,column=0)
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
e1=Entry(root,textvariable=v1).grid(row=2,column=1)
e2=Entry(root,textvariable=v2).grid(row=4,column=1)
e3=Entry(root,textvariable=v3).grid(row=6,column=1)
e4=Entry(root,textvariable=v4).grid(row=8,column=1)
Label(root,text='').grid(row=9,column=0)
             
def insert():
    adno=v1.get()
    name=v2.get()
    cl=v3.get()
    mob=v4.get()
    my_cur=db.cursor()
    my_cur.execute('insert into student values(%s,%s,%s,%s)',
                       (adno,name,cl,mob))
    db.commit()
    messagebox.showinfo('Awesome!!!!','1 record inserted')
    v1.set('')
    v2.set('')
    v3.set('')
    v4.set('')

def clear():
    v1.set('')
    v2.set('')
    v3.set('')
    v4.set('')

def close():
    root.destroy()
Button(root,text='SUBMIT',command=insert).grid(row=10,column=0)
Button(root,text='RESET',command=clear).grid(row=10,column=1)
Button(root,text='EXIT',command=close).grid(row=10,column=2)
root.mainloop()

