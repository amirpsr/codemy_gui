from tkinter import *

root = Tk()
root.title("First program")

e= Entry(root, width= 45 ,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)

def number_holder(number):
    return

button_1 = Button(root,text="1", padx=40 , pady=20, command = number_holder)
button_2 = Button(root,text="2", padx=40 , pady=20, command = number_holder)
button_3 = Button(root,text="3", padx=40 , pady=20, command = number_holder)
button_4 = Button(root,text="4", padx=40 , pady=20, command = number_holder)
button_5 = Button(root,text="5", padx=40 , pady=20, command = number_holder)
button_6 = Button(root,text="6", padx=40 , pady=20, command = number_holder)
button_7 = Button(root,text="7", padx=40 , pady=20, command = number_holder)
button_8 = Button(root,text="8", padx=40 , pady=20, command = number_holder)
button_9 = Button(root,text="9", padx=40 , pady=20, command = number_holder)
button_0 = Button(root,text="0", padx=40 , pady=20, command = number_holder)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)


root.mainloop()