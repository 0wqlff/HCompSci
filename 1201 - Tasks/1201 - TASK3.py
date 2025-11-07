password=input("Please enter a password: ")
while (ord(password[0:1])<65 or ord(password[0:1])>90 or ord(password[-1:len(password)])<35 or ord(password[-1:len(password)])>37):
    if (ord(password[0:1])>=65 and ord(password[0:1])<=90):
        print("Your password begins with a capital letter. Good!")
    elif (ord(password[-1:len(password)])>=35 and ord(password[-1:len(password)])<=37):
        print("Your password ends with a symbol. Good!")
    print("This password is not secure. Try again.")
    password=input("Please enter a password: ")
print("""Your password begins with a capital letter. Good!
Your password ends with a symbol. Good!
This password is secure. Well done.
    """)

