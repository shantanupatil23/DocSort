from tkinter import*
root=Tk()
ques=["Practice questions 1","Practice questions 2","Practice questions 3","Important questions 1","Important questions 2"]
button1=Button(root,text=ques[0],fg="black")
button2=Button(root,text=ques[1],fg="black")
button3=Button(root,text=ques[2],fg="black")
button4=Button(root,text=ques[3],fg="black")
button5=Button(root,text=ques[4],fg="black")

label1=Label(root,text="Select a File")
label1.grid(row=50)
button1.grid(row=51)
button2.grid(row=52)
button3.grid(row=53)
button4.grid(row=54)
button5.grid(row=55)
root.mainloop()
