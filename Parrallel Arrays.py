#206 Parallel Arrays - Task 3

# Write a program that will ask the user for their name and a test mark out of 100.
 
# This should be looped five times and the names and marks should be stored in separate arrays. 

# Print out the contents of the names and the marks arrays. 

# def get_name():
#     names=str(input("What is your name? "))
#     return names

# def get_test():
#     marks=int(input("How many marks did you get? "))
#     while (marks>100 or marks<0):
#         print("NUH UH")
#         marks=int(input("How many marks did you get? "))
#     return marks

# def display_all(n,m):
#     for i in range(5):
#         print(n[i] + " scored " + str(m[i]))

# name=[]
# mark=[]
# for index in range(5):
#     name.append(get_name())
#     mark.append(get_test())
# display_all(name,mark)



from dataclasses import dataclass
@dataclass
class PERSON():
    name : str = ''
    mark : int = 0
    

def get_name():
    names=str(input("What is your name? "))
    return names

def get_test():
    marks=int(input("How many marks did you get? "))
    while (marks>100 or marks<0):
        print("NUH UH")
        marks=int(input("How many marks did you get? "))
    return marks

def display_all(people):
    for i in range(5):
        print(people[i] + " scored " + str(people[i]))

people = [PERSON(),PERSON(),PERSON(),PERSON(),PERSON()]
for index in range(5):
    name.append(get_name())
    mark.append(get_test())
display_all(name,mark)

