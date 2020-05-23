from tkinter import*
root=Tk()
lab_ass=["Lab Assignment 1","Lab Assignment 2","Lab Assignment 3","Lab Assignment 4","Lab Assignment 5"]
button1=Button(root,text=lab_ass[0],fg="black")
button2=Button(root,text=lab_ass[1],fg="black")
button3=Button(root,text=lab_ass[2],fg="black")
button4=Button(root,text=lab_ass[3],fg="black")
button5=Button(root,text=lab_ass[4],fg="black")

label1=Label(root,text="Select a Lab Assignment")
label1.grid(row=50)
button1.grid(row=51)
button2.grid(row=52)
button3.grid(row=53)
button4.grid(row=54)
button5.grid(row=55)
root.mainloop()
