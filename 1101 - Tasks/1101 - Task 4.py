names = ["John","Joan","Mark","Michael"]
months = ["May","May","May","May","May"]
ages = [23,35,23,8]

with open("1101 - Tasks/names.txt","w") as wfile:
    for counter in range(0,len(names)):
        wfile.write(names[counter] + "," + str(months[counter]) + "," + str(ages[counter])+"\n")
