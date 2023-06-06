# Python program to  create a simple GUI  
# calculator using Tkinter 
  
# import everything from tkinter module 
from tkinter import *
  
# globally declare the expression variable 
expression = "" 
  
  
# Function to update expressiom 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
  
    # concatenation of string 
    expression = expression + str(num) 
  
    # update the expression by using set method 
    equation.set(expression) 
  
  
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
    try: 
  
        global expression 
  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
  
        equation.set(total) 
  
        # initialze the expression variable 
        # by empty string 
        expression = "" 
  
    # if error is generate then handle 
    # by the except block 
    except: 
  
        equation.set(" error ") 
        expression = "" 
  
  
# Function to clear the contents 
# of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
  
  
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
  
    # set the background colour of GUI window 
    gui.configure(background="light green") 
  
    # set the title of GUI window 
    gui.title("Simple Calculator") 
  
    # set the configuration of GUI window 
    gui.geometry("400x380") 
  
    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar() 
  
    # create the text entry box for 
    # showing the expression . 
    expression_field = Entry(gui, textvariable=equation,width=40) 
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    expression_field.place(x=60,y=50) 
  
    equation.set('enter your expression') 
  
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    button1 = Button(gui, text=' 1 ', fg='black', bg='DodgerBlue', 
                     command=lambda: press(1), height=1, width=7) 
    button1.place(x=30,y=100) 
  
    button2 = Button(gui, text=' 2 ', fg='black', bg='DodgerBlue', 
                     command=lambda: press(2), height=1, width=7) 
    button2.place(x=110,y=100) 
  
    button3 = Button(gui, text=' 3 ', fg='black', bg='DodgerBlue', 
                     command=lambda: press(3), height=1, width=7) 
    button3.place(x=190,y=100) 
  
    button4 = Button(gui, text=' 4 ', fg='black', bg='DodgerBlue', 
                     command=lambda: press(4), height=1, width=7) 
    button4.place(x=30,y=130) 
  
    button5 = Button(gui, text=' 5 ', fg='black', bg='DodgerBlue', 
                     command=lambda: press(5), height=1, width=7) 
    button5.place(x=110,y=130) 
  
    button6 = Button(gui, text=' 6 ', fg='black', bg='DodgerBlue', 
                     command=lambda: press(6), height=1, width=7) 
    button6.place(x=190,y=130) 
  
    button7 = Button(gui, text=' 7 ', fg='black', bg='DodgerBlue', 
                     command=lambda: press(7), height=1, width=7) 
    button7.place(x=30,y=160) 
  
    button8 = Button(gui, text=' 8 ', fg='black', bg='DodgerBlue', 
                     command=lambda: press(8), height=1, width=7) 
    button8.place(x=110,y=160) 
  
    button9 = Button(gui, text=' 9 ', fg='black', bg='DodgerBlue', 
                     command=lambda: press(9), height=1, width=7) 
    button9.place(x=190,y=160) 
  
    button0 = Button(gui, text=' 0 ', fg='black', bg='DodgerBlue', 
                     command=lambda: press(0), height=1, width=7) 
    button0.place(x=30,y=190)

    button9 = Button(gui, text='Exit ', fg='black', bg='DimGrey', 
                     command=gui.destroy, height=1, width=7) 
    button9.place(x=150,y=280)     
  
    plus = Button(gui, text=' + ', fg='black', bg='DodgerBlue', 
                  command=lambda: press("+"), height=1, width=7) 
    plus.place(x=270,y=100) 
  
    minus = Button(gui, text=' - ', fg='black', bg='DodgerBlue', 
                   command=lambda: press("-"), height=1, width=7) 
    minus.place(x=270,y=130) 
  
    multiply = Button(gui, text=' * ', fg='black', bg='DodgerBlue', 
                      command=lambda: press("*"), height=1, width=7) 
    multiply.place(x=270,y=160) 
  
    divide = Button(gui, text=' / ', fg='black', bg='DodgerBlue', 
                    command=lambda: press("/"), height=1, width=7) 
    divide.place(x=270,y=190)  
  
    equal = Button(gui, text=' = ', fg='black', bg='DodgerBlue', 
                   command=equalpress, height=1, width=7) 
    equal.place(x=190,y=190)  
  
    clear = Button(gui, text='Clear', fg='black', bg='DodgerBlue', 
                   command=clear, height=1, width=7) 
    clear.place(x=110,y=190)  
  
    # start the GUI 
    gui.mainloop() 
