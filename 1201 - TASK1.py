password=input("Please enter password ")
passwords=list(password)
total=0
for i in range(len(passwords)):
    total+=ord(passwords[i])
total=total%11
password=password+str(total)
print("The new password is",password)