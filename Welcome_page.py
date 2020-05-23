from tkinter import *
root=Tk()
title=Label(root, text="WELCOME", fg="Black")
title.grid(row=0, columnspan=2)
button1=Button(root,text="Login",fg="Red")
button2=Button(root,text="Guest",fg="Blue")
button1.grid(row=1,rowspan=2)
button2.grid(row=3,rowspan=2)
root.mainloop()