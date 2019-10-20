# In normal case, these things will be read from file
subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
subject1_units = ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5"]
notes_11 = []  # "subject""unit" For notes


# def add_new_note(choise):
#     Will do it later

# Functions for opening file of particular unit (through GUI)
# choose_notes_from_"subject number""Unit number"


def choose_notes_from_11():
    print(list(notes_11))
    

# There functions is only used for accessing program without GUI

def choose_unit_from_1():
    print("Available units:")
    for i in range(0, len(subject1_units)):
        print(f"{i + 1}. {subject1_units[i]}")
    print()
    unit = input("Which unit to open? (1-5) ")
    unit = int(unit)
    if unit == 1:
        choose_notes_from_11()
    elif unit == 2:
        choose_notes_from_12()
    elif unit == 3:
        choose_notes_from_13()
    elif unit == 4:
        choose_notes_from_14()
    elif unit == 5:
        choose_notes_from_15()


def choose_subject():
    print("Available subjects:")
    for i in range(0, len(subjects)):
        print(f"{i + 1}. {subjects[i]}")
    print()
    subject = input("Which subject to open? (1-5) ")
    subject = int(subject)
    if subject == 1:
        choose_unit_from_1()
    elif subject == 2:
        choose_unit_from_2()
    elif subject == 3:
        choose_unit_from_3()
    elif subject == 4:
        choose_unit_from_4()
    elif subject == 5:
        choose_unit_from_5()


# For logging in

def guest_login():
    print("Logged in as Guest...\n")
    choose_subject()


def admin_login():
    print("Logged in as Admin...\n")
    choose_subject()


inputDetected = False
while not inputDetected:
    user = input("Run as Administrator? (y/n) ")
    if user == "n":
        inputDetected = True
        guest_login()
    elif user == "y":
        password = input("Enter password: ")
        if password == "password":
            inputDetected = True
            admin_login()
        else:
            print("Enter Valid Password or login as Guest")
