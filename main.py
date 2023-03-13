from student_details import data1, data2

bol = True
while bol:
    bol1 = True
    while bol1:
        usr_input = input(f"Press 1 to search student information.\nPress 2 to enter details of new user.\n")
        if usr_input == '1':
            search_criteria = input("What you want to search from (roll number or name) of the student? ")
            bol1 = False
        elif usr_input == '2':
            print("Please enter your details below. ")
            name = input("Please enter your name. ")
            e_mail = input("Please enter your email id.")
            roll_no = input("Please enter the roll number . ")
            hostel = input("Please enter the hostel and room number. ")
            grp = input("Please enter your Group details. ")
            f_name = input("Please enter your fathers name. ")
            no = input("Please enter the contact number. ")
            data1[name] = [name, e_mail, hostel, grp, f_name, no, roll_no]
            data1[roll_no] = [name, e_mail, hostel, grp, f_name, no, roll_no]
            should_continue = input("Press 1 to continue or Press ant key to search again.  ")
            if should_continue == "1":
                bol1 = False
                search_criteria = input("What you want to search from (roll number or name) of the student? ")

    bol2 = True
    while bol2:
        if search_criteria == "name":
            data = data1
            bol2 = False
        elif search_criteria == "roll number":
            data = data2
            bol2 = False
        else:
            print("Enter Valid Information")
            search_criteria = input("What you want to search from (roll number or name) of the student? ")

    user_input = input(f"Please enter {search_criteria} of the user? ").lower()
    bol = False
    for key in data:
        if user_input == key:
            bol = True

    if not bol:
        print("Sorry we dont have information on that user. ")
        exit()

    # Asking the user what information he wants
    next_bol = True
    while next_bol:
        print("Press 1 for email id. ")
        print("Press 2 for room number. ")
        print("Press 3 for group information. ")
        print("Press 4 for Father name. ")
        print("Press 5 for Phone Number. ")
        print("Press 6 for displaying all information all together. ")
        user_ask = int(input("Please select your desired input. "))

        # if user_ask == "email id" or "phone number" or "room number" or "attendance" or "group information":
        if user_ask == 1:
            print(data[user_input][1])
        elif user_ask == 5:
            print(data[user_input][5])
        elif user_ask == 2:
            print(data[user_input][2])
        elif user_ask == 3:
            print(data[user_input][3])
        elif user_ask == 4:
            print(data[user_input][5])
        elif user_ask == 5:
            print(data[user_input][4])
        elif user_ask == 6:
            print(
                f" Name: {data[user_input][0]}\n Group Number: {data[user_input][3]}\n Room number: {data[user_input][2]}\n"
                f" Father name: {data[user_input][5]}\n Phone number: {data[user_input][4]}\n Email id: {data[user_input][1]}\n")
        else:
            print("we dont have info on that user")

        exit_loop = input("press 12 to the program else press any other key ")
        if exit_loop == "12":
            next_bol = False
