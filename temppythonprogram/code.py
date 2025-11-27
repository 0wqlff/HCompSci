from dataclasses import dataclass
@dataclass
class TEMP():
    day:str=""
    dayTemp:float=0.0
temperatures=[TEMP() for i in range(14)]

def getday():
    day=str(input("What day is the temperature for? "))
    return day

def getdayTemp():
    dayTemp=float(input("What was the temperature? " ))
    while (dayTemp > 50 or dayTemp < -20):
        print("please enter a valid temperature")
        dayTemp=float(input("What was the temperature? " ))
    return dayTemp

def arrayofrecord(temperatures):
    for i in range (14):
        temperatures[i].day=getday()
        temperatures[i].dayTemp=getdayTemp()
    return temperatures

def findminmax(temperatures):
    minimum=temperatures[0].dayTemp
    maximum= temperatures[0].dayTemp
    for i in range(14):
        if (temperatures[i].dayTemp > maximum):
            maximum = temperatures[i].dayTemp
        elif (temperatures[i].dayTemp < minimum):
            minimum = temperatures[i].dayTemp
    return minimum, maximum

def calcavgtemp():
    total=0
    for i in range(14):
        total+=temperatures[i].dayTemp
    total=total/14
    with open("temppythonprogram/avgtemp.txt","w") as writefile:
        writefile.write(str(total))
    return total


def display(temperatures):
    for i in range(14):
        print(temperatures[i].dayTemp)
    minimum , maximum = findminmax(temperatures)
    avgtemp = calcavgtemp()
    print(minimum)
    print(maximum)
    print(avgtemp)
    
arrayofrecord(temperatures)
display(temperatures)


