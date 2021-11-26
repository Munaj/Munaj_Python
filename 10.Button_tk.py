﻿from tkinter import *

root = Tk()
e = Entry(root,width = 20,borderwidth = 5)
e.grid(row=0,column= 0,columnspan = 3,padx = 10,pady=10)

def button_click(number): 
    current_var = e.get()
    e.delete(0,END)
    e.insert(0,f"{current_var}{number}")
    return
def button_del():
    e.delete(0,END)

button_0 = Button(root,text= "0",padx=20,pady= 20, command= lambda: button_click(0))
button_1 = Button(root,text= "1",padx=20,pady= 20, command= lambda: button_click(1))
button_2 = Button(root,text= "2",padx=20,pady= 20, command= lambda: button_click(2))
button_3 = Button(root,text= "3",padx=20,pady= 20, command= lambda: button_click(3))
button_4 = Button(root,text= "4",padx=20,pady= 20, command= lambda: button_click(4))
button_5 = Button(root,text= "5",padx=20,pady= 20, command= lambda: button_click(5))
button_6 = Button(root,text= "6",padx=20,pady= 20, command= lambda: button_click(6))
button_7 = Button(root,text= "7",padx=20,pady= 20, command= lambda: button_click(7))
button_8 = Button(root,text= "8",padx=20,pady= 20, command= lambda: button_click(8))
button_9 = Button(root,text= "9",padx=20,pady= 20, command= lambda: button_click(9))

button_add = Button(root,text= "+",padx=20,pady= 20, command= lambda: button_click(9))
button_dell = Button(root,text= "CLR",padx=12,pady= 20, command= lambda: button_del())

button_0.grid(row=5, column=0)
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_add.grid(row=5,column=1)
button_dell.grid(row=5,column=2)
    




root.mainloop()