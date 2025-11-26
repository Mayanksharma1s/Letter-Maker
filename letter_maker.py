name = input("Please Enter your Name: ")
date = input("Please Enter the Date you want in the Letter: ")
# --- Ask user whether they want Formal or Informal Letter ---
while True:

    try:
        letter_type = int(input("Please select 1 if you want formal letter\nAnd 2 if you want informal letter: "))
        if 0 < letter_type <= 2: # Check valid input 1 or 2
            print("So your selection is", letter_type)
            break
        else:
            print("Please only select 1 or 2")
    except ValueError:
        print("Please only select 1 or 2 Integer")
 # --- Ask user whether they want Principal or Teacher or Editor Letter ---
if letter_type == 1:
    while True:
        try:
            to_whom = int(input("If you want to send to principal type 1\nIf Teacher press 2\nIf Editor press 3"))
            if 1 <= to_whom <= 3:
                break
            else:
                print("Please select only integer 1, 2 or 3")
        except ValueError:
            print("Please only select Integer 1, 2 or 3")
    # --- Output for Principal --- 
    if to_whom == 1:
        subject_p = input("Please enter the Subject for the Letter: ")
        content_p = input("Please enter the content inside the Letter: ")
        school_name_p = input("Please input your School name: ")
        print(f"The Principal\n{school_name_p}\n\nDate: {date}\n\nSubject - {subject_p}\n\nRespected Sir/Madam,\n{content_p}\nThanking you.\nYours obediently,\n{name}")
    # --- Output for Teacher ---
    elif to_whom == 2:
        subject_t = input("Please enter the Subject for the Letter: ")
        content_t = input("Please enter the content for the Letter: ")
        school_name_t = input("Please input your School name: ")
        print(f"The Teacher\n{school_name_t}\n\n{date}\n\nSubject - {subject_t}\nRespected Sir/Madam,\n\n{content_t}\nThanking you.\n\nYours Obediently,\n{name}")
    # --- Output for Editor ---
    else:
        sender_add = input("Please enter your address: ")
        editor_name = input("Enter the name of Editor: ")
        editor_add = input("Enter editor's address: ")
        subject_e = input("Enter the subject of the Letter: ")
        content_e = input("Enter the content inside the Letter: ")
        print(f"{sender_add}\n\n{date}\n\nThe Editor,\n{editor_name}\n{editor_add}\n\nSubject - {subject_e}\n\nRespected Sir/Madam,\n{content_e}\nThanking you.\n\nYours faithfully,{name}")
# --- Informal Letter ---
else:
    your_add = input("Please Enter your address:")
    to_send = input("To whom you want to send the letter: ")
    content = input("Please enter the content inside the letter: ")
    print(f"{your_add}\n\n{date}\n\nDear {to_send},\n{content}\n\nYours {name}")
