# In normal case, these things will be read from file
subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]
subject1_units = ["Unit 1", "Unit 2", "Unit 3", "Unit 4", "Unit 5"]
11 = []  # "subject""unit" For notes


def add_new_note(choise):
    choise


# Functions for opening file of particular unit (through GUI)
# choose_notes_from_"subject number""Unit number"


def choose_notes_from_11():
    print(list(subject1_unit1_notes))


def choose_notes_from_12():
    print(list(subject1_unit2_notes))


def choose_notes_from_13():
    print(list(subject1_unit3_notes))


def choose_notes_from_14():
    print(list(subject1_unit4_notes))


def choose_notes_from_15():
    print(list(subject1_unit5_notes))


def choose_notes_from_21():
    print(list(subject2_unit1_notes))


def choose_notes_from_22():
    print(list(subject2_unit2_notes))


def choose_notes_from_23():
    print(list(subject2_unit3_notes))


def choose_notes_from_24():
    print(list(subject2_unit4_notes))


def choose_notes_from_25():
    print(list(subject2_unit5_notes))


def choose_notes_from_31():
    print(list(subject3_unit1_notes))


def choose_notes_from_32():
    print(list(subject3_unit2_notes))


def choose_notes_from_33():
    print(list(subject3_unit3_notes))


def choose_notes_from_34():
    print(list(subject3_unit4_notes))


def choose_notes_from_35():
    print(list(subject3_unit5_notes))


def choose_notes_from_41():
    print(list(subject4_unit1_notes))


def choose_notes_from_42():
    print(list(subject4_unit2_notes))


def choose_notes_from_43():
    print(list(subject4_unit3_notes))


def choose_notes_from_44():
    print(list(subject4_unit4_notes))


def choose_notes_from_45():
    print(list(subject4_unit5_notes))


def choose_notes_from_51():
    print(list(subject5_unit1_notes))


def choose_notes_from_52():
    print(list(subject5_unit2_notes))


def choose_notes_from_53():
    print(list(subject5_unit3_notes))


def choose_notes_from_54():
    print(list(subject5_unit4_notes))


def choose_notes_from_55():
    print(list(subject5_unit5_notes))


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


def choose_unit_from_2():
    print("Available units:")
    for i in range(0, len(subject2_units)):
        print(f"{i + 1}. {subject2_units[i]}")
    print()
    unit = input("Which unit to open? (1-5) ")
    unit = int(unit)
    if unit == 1:
        choose_notes_from_21()
    elif unit == 2:
        choose_notes_from_22()
    elif unit == 3:
        choose_notes_from_23()
    elif unit == 4:
        choose_notes_from_24()
    elif unit == 5:
        choose_notes_from_25()


def choose_unit_from_3():
    print("Available units:")
    for i in range(0, len(subject3_units)):
        print(f"{i + 1}. {subject3_units[i]}")
    print()
    unit = input("Which unit to open? (1-5) ")
    unit = int(unit)
    if unit == 1:
        choose_notes_from_31()
    elif unit == 2:
        choose_notes_from_32()
    elif unit == 3:
        choose_notes_from_33()
    elif unit == 4:
        choose_notes_from_34()
    elif unit == 5:
        choose_notes_from_35()


def choose_unit_from_4():
    print("Available units:")
    for i in range(0, len(subject4_units)):
        print(f"{i + 1}. {subject4_units[i]}")
    print()
    unit = input("Which unit to open? (1-5) ")
    unit = int(unit)
    if unit == 1:
        choose_notes_from_41()
    elif unit == 2:
        choose_notes_from_42()
    elif unit == 3:
        choose_notes_from_43()
    elif unit == 4:
        choose_notes_from_44()
    elif unit == 5:
        choose_notes_from_45()


def choose_unit_from_5():
    print("Available units:")
    for i in range(0, len(subject5_units)):
        print(f"{i + 1}. {subject5_units[i]}")
    print()
    unit = input("Which unit to open? (1-5) ")
    unit = int(unit)
    if unit == 1:
        choose_notes_from_51()
    elif unit == 2:
        choose_notes_from_52()
    elif unit == 3:
        choose_notes_from_53()
    elif unit == 4:
        choose_notes_from_54()
    elif unit == 5:
        choose_notes_from_55()


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

def guest():
    print("Logged in as Guest...\n")
    choose_subject()


def admin():
    print("Logged in as Admin...\n")
    choose_subject()


inputDetected = False
while not inputDetected:
    user = input("Run as Administrator? (y/n) ")
    if user == "n":
        inputDetected = True
        guest()
    elif user == "y":
        password = input("Enter password: ")
        if password == "password":
            inputDetected = True
            admin()
        else:
            print("Enter Valid Password or login as Guest")
