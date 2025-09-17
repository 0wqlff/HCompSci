#Decorators Assistance
def getuserinput():
    l=int(input("Enter length: "))
    b=int(input("Enter breadth: "))
    h=int(input("Enter height: "))
    return l,b,h

def calculateroom(length, breadth, height):
    w=2*length*height + 2*breadth*height
    f=breadth*length
    return w,f


def calculatereqs(wall, floor):
    wallpaperreq = wall/1
    carpetreq = floor/1
    paintreq = floor/1
    return wallpaperreq, carpetreq, paintreq


def output(wallpaperreq, carpetreq, paintreq):
    print("You will need", wallpaperreq,"rolls of wallpaper")
    print("You need", carpetreq, "tiles carpet")
    print("You need", paintreq, "litres of paint")



length, breadth, height = getuserinput()
wall, floor = calculateroom(length, breadth, height)
wallpaperreq, carpetreq, paintreq = calculatereqs(wall, floor)
output(wallpaperreq, carpetreq, paintreq)