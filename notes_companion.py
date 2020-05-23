from tkinter import *
import os
import os.path

password = 'default'
admin = False
subject_called = 'null'
option_called = 'null'
unit_called = 'null'
correct_password = 'soe@123'
subject_names = ["Data Structures (DS)", "Discrete Mathematics (DM)", "Economics and Finance for Engineers (EFE)", "Digital and Electronic Logic Design (DELD)", "Computer Organisation and Microprocessing Interface (COMI)"]


def open_doc():
    file_type = 'null'
    found = True

    if os.path.isfile(f'D:\\MP\\{subject_called}_{option_called}_{unit_called}.pdf') is True:
        file_type = 'pdf'
    elif os.path.isfile(f'D:\\MP\\{subject_called}_{option_called}_{unit_called}.jpg') is True:
        file_type = 'jpg'
    elif os.path.isfile(f'D:\\MP\\{subject_called}_{option_called}_{unit_called}.docx') is True:
        file_type = 'docx'
    elif os.path.isfile(f'D:\\MP\\{subject_called}_{option_called}_{unit_called}.ppt') is True:
        file_type = 'ppt'
    elif os.path.isfile(f'D:\\MP\\{subject_called}_{option_called}_{unit_called}.pptx') is True:
        file_type = 'pptx'
    elif os.path.isfile(f'D:\\MP\\{subject_called}_{option_called}_{unit_called}.jpeg') is True:
        file_type = 'jpeg'
    elif os.path.isfile(f'D:\\MP\\{subject_called}_{option_called}_{unit_called}.cpp') is True:
        file_type = 'cpp'
    elif os.path.isfile(f'D:\\MP\\{subject_called}_{option_called}_{unit_called}.gslides') is True:
        file_type = 'gslides'
    else:
        # file not found window
        found = False
    if found:
        os.system(f'D:\\MP\\{subject_called}_{option_called}_{unit_called}.{file_type}')


def show_notes():
    print('')
    # Incomplete


def show_lab():
    print('')
    # Incomplete


def show_assignment():
    print('')
    # Incomplete


def show_que():
    print('')
    # Incomplete


def display_options():
    global root
    root = Tk()
    notes_button = Button(root, text='Notes', fg='black', command=show_notes)
    notes_button.grid(row=50, column=50)
    lab_button = Button(root, text='Lab', fg='black', command=show_lab)
    lab_button.grid(row=51, column=50)
    assignment_button = Button(root, text='Assignment', fg='black', command=show_assignment)
    assignment_button.grid(row=52, column=50)
    que_button = Button(root, text='Practice & Important Questions', fg='black', command=show_que)
    que_button.grid(row=53, column=50)
    root.mainloop()


def temp_ds():
    global subject_called
    subject_called = 'ds'
    display_options()


def temp_dm():
    global subject_called
    subject_called = 'dm'
    display_options()


def temp_efe():
    global subject_called
    subject_called = 'efe'
    display_options()


def temp_deld():
    global subject_called
    subject_called = 'deld'
    display_options()


def temp_comi():
    global subject_called
    subject_called = 'comi'
    display_options()


def main_menu():
    global root
    root = Tk()
    global subject_names
    ds_button = Button(root, text=subject_names[0], fg="black", command=temp_ds)
    dm_button = Button(root, text=subject_names[1], fg="black", command=temp_dm)
    efe_button = Button(root, text=subject_names[2], fg="black", command=temp_efe)
    deld_button = Button(root, text=subject_names[3], fg="black", command=temp_deld)
    comi_button = Button(root, text=subject_names[4], fg="black", command=temp_comi)
    label = Label(root, text="Select a Subject", fg="red")
    label.grid(row=49, column=50)
    ds_button.grid(row=50, column=50)
    dm_button.grid(row=51, column=50)
    efe_button.grid(row=52, column=50)
    deld_button.grid(row=53, column=50)
    comi_button.grid(row=54, column=50)
    root.mainloop()


def admin_login():
    def check_password():
        global root
        global admin
        global password
        global correct_password
        password = entry1.get()
        if password == correct_password:
            admin = True
            main_menu()
        else:
            root = Tk()
            label = Label(root, text="Wrong password", fg="black")
            label.grid(row=4, column=4, columnspan=3)
            root.mainloop()
    root = Tk()
    label1 = Label(root, text="Enter the password", fg="black")
    entry1 = Entry(root)
    button1 = Button(root, text="login", fg="red", command=check_password)
    label1.grid(row=4, column=4, columnspan=3)
    entry1.grid(row=5, column=5)
    button1.grid(row=8, column=5)
    root.mainloop()


def welcome_page():
    global root
    root = Tk()
    title = Label(root, text="WELCOME", fg="Black")
    title.grid(row=0, columnspan=2)
    admin_button = Button(root, text="Login", fg="Red", command=admin_login)
    guest_button = Button(root, text="Guest", fg="Blue", command=main_menu)
    admin_button.grid(row=1, rowspan=2)
    guest_button.grid(row=3, rowspan=2)
    root.mainloop()


# welcome_page()
open_doc()
