password = input("please enter your password:")
vpassword = input("please enter your verification password:")
count = 0
if password != vpassword:
    count += 1
    while password != vpassword:
        password = input("please enter your password:")
        vpassword = input("please enter your verification password:")

        count += 1

        if count == 5:
            print("you had too many failed attempts , access denied.")








else:
    print("you have entered successfully!")
