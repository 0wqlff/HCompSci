with open("1101 - Tasks/Runners.txt") as readfile:
    line = readfile.readline().rstrip('\n')
    time = line.split(", ")[1]
    while line : 
        items = line.split(", ")
        if items[1]<time:
            time=items[1]
            name=items[0]
        line = readfile.readline().rstrip('\n')
print("The fastest runner was " + name + " who ran 100m in " + str(time) + " seconds.")

