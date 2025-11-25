from tkinter import *
from tkinter import ttk
import re

# window config constant
win_height = 400
win_width = 300

# labels, buttons constants
lab_height = 5
lab_width = 5

btn_height = 30
btn_width = 60

# window
window = Tk()
window.title("Calculator")
window.config(background="#D6F4ED")
window.minsize(height=win_height,width=win_width)

label_var = StringVar()
label_var.set("")

# pattern check for calculation
# pat =

def calc(var):
    try:
        result = eval(var)
        label_var.set(result)
        print(result)
    except:
        label_var.set("Error")
        print("error")

def clr():
    global label_var
    label_var.set("")

# function that shows calculation in label
def show_calc(t):
    curr_var = label_var.get()
    new_var = curr_var + t

    if t == "=":
        calc(curr_var)
    else:
        label_var.set(new_var)

# calculation and result panel
calc_show = Label(bg="white",textvariable=label_var, state="disabled",height=1,width=15,border=2,text="0", font=("Arial", 30, "bold"), justify="right")
calc_show.grid(row=0,column=0, columnspan=4,rowspan=1)

# buttons
b1 = Button(fg="#53629E", text="1", height=1,width=5,font=("Arial", 10, "bold"), justify="center", command=lambda: show_calc("1"))
b1.grid(row=2,column=0,pady=5)

b2 = Button(fg="#53629E", text="2", height=1,width=5,font=("Arial", 10, "bold"), justify="center", command=lambda: show_calc("2"))
b2.grid(row=2,column=1,pady=5)

b3 = Button(fg="#53629E", text="3", height=1,width=5,font=("Arial", 10, "bold"), justify="center", command=lambda: show_calc("3"))
b3.grid(row=2,column=2,pady=5)

b4 = Button(fg="#53629E", text="4", height=1,width=5,font=("Arial", 10, "bold"), justify="center", command=lambda: show_calc("4"))
b4.grid(row=3,column=0,pady=5)

b5 = Button(fg="#53629E", text="5", height=1,width=5,font=("Arial", 10, "bold"), justify="center", command=lambda: show_calc("5"))
b5.grid(row=3,column=1,pady=5)

b6 = Button(fg="#53629E", text="6", height=1,width=5,font=("Arial", 10, "bold"), justify="center", command=lambda: show_calc("6"))
b6.grid(row=3,column=2,pady=5)

b7 = Button(fg="#53629E", text="7", height=1,width=5,font=("Arial", 10, "bold"), justify="center", command=lambda: show_calc("7"))
b7.grid(row=4,column=0,pady=5)

b8 = Button(fg="#53629E", text="8", height=1,width=5,font=("Arial", 10, "bold"), justify="center", command=lambda: show_calc("8"))
b8.grid(row=4,column=1,pady=5)

b9 = Button(fg="#53629E", text="9", height=1,width=5,font=("Arial", 10, "bold"), justify="center", command=lambda: show_calc("9"))
b9.grid(row=4,column=2,pady=5)

b0 = Button(fg="#53629E", text="0", height=1,width=5,font=("Arial", 10, "bold"), justify="center", command=lambda: show_calc("0"))
b0.grid(row=5,column=1,pady=5)

# operations button
b_add = Button(fg="#53629E", text="+", height=1,width=5,font=("Arial", 18, "bold"), justify="center", command=lambda: show_calc("+"))
b_add.grid(row=2,column=3,pady=5)

b_sub = Button(fg="#53629E", text="-", height=1,width=5,font=("Arial", 18, "bold"), justify="center", command=lambda: show_calc("-"))
b_sub.grid(row=3,column=3,pady=5)

b_div = Button(fg="#53629E", text="/", height=1,width=5,font=("Arial", 18, "bold"), justify="center", command=lambda: show_calc("/"))
b_div.grid(row=4,column=3,pady=5)

b_mul = Button(fg="#53629E", text="*", height=1,width=5,font=("Arial", 18, "bold"), justify="center", command=lambda: show_calc("*"))
b_mul.grid(row=5,column=3,pady=5)

b_eql = Button(fg="#53629E", text="=", height=1,width=5,font=("Arial", 18, "bold"), justify="center", command=lambda: show_calc("="))
b_eql.grid(row=6,column=3,pady=5)

b_clr = Button(fg="#53629E", text="Clear", height=1,width=5,font=("Arial", 18, "bold"), justify="center", command=clr)
b_clr.grid(row=6,column=1,pady=5)


# mainloop
window.mainloop()