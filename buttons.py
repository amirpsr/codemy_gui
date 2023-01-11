from tkinter import *

root = Tk()
root.title("First program")

e= Entry(root, width=100 , bg = "blue" )
e.pack()
e.insert(0,"enter your name")
def my_click():
    my_label = Label(root,text ="hello " + e.get())
    my_label.pack()

my_button1 = Button(root,text="enter your name!",padx=50,pady=50 , command=my_click , fg="blue", bg="red")
my_button1.pack() 

root.mainloop()
