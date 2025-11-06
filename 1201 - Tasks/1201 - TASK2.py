def replace_letter(animal):
    if (ord(animal[0:1]) >= 97 and ord(animal[0:1]) <= 122):
        print(chr(ord(animal[0:1])-32)+animal[1:])
    else:
        print(animal)

animal=input("Please enter the name of an animal ")
replace_letter(animal)
