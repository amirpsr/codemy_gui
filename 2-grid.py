from tkinter import *

root = Tk()
root.title("First program")
my_label1 = Label(root, text="Hello world!")
my_label2 = Label(root, text="Hello world!")

my_label1.grid(row=0 , column=0)
my_label2.grid(row=1 , column=1)

root.mainloop()