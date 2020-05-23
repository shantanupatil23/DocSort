from tkinter import *

root = Tk()
label1 = Label(root, text="Enter the password", fg="black")
entry1 = Entry(root)
button1 = Button(root, text="login", fg="red")
label1.grid(row=4, column=4, columnspan=3)
entry1.grid(row=5, column=5)
button1.grid(row=8, column=5)

root.mainloop()
