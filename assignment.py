from tkinter import*
root=Tk()
ass=["Assignment 1","Assignment 2","Assignment 3","Assignment 4","Assignment 5"]
button1=Button(root,text=ass[0],fg="black")
button2=Button(root,text=ass[1],fg="black")
button3=Button(root,text=ass[2],fg="black")
button4=Button(root,text=ass[3],fg="black")
button5=Button(root,text=ass[4],fg="black")

label1=Label(root,text="Select an Assignment")
label1.grid(row=50)
button1.grid(row=51)
button2.grid(row=52)
button3.grid(row=53)
button4.grid(row=54)
button5.grid(row=55)
root.mainloop()
