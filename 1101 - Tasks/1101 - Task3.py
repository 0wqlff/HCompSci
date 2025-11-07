items = []
names = []
marks = []
with open("1101 - Tasks./pupils.txt") as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
        items = line.split(",")
        names.append(items[0])
        marks.append(items[1])
        line = readfile.readline().rstrip('\n')
for i in range(len(names)):
    print(names[i]+" -"+marks[i])