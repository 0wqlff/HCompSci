import time
with open("rick.txt") as readfile:
    music=readfile.readline()
    while music!="":
        print(music.strip())
        time.sleep(2)
        music=readfile.readline()