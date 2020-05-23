from tkinter import *
root= Tk()
button1=Button(root,text="Notes",fg="black")
button2=Button(root,text="Assignment",fg="black")
button3=Button(root,text="Lab",fg="black")
button4=Button(root,text="Practice & Important Questions ",fg="black")
button1.grid(row=50,column=50)
button2.grid(row=51,column=50)
button3.grid(row=52,column=50)
button4.grid(row=53,column=50)

root.mainloop()
