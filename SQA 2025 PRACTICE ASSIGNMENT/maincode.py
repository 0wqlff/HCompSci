from dataclasses import dataclass
class order():
    orderNum : str = ""
    date : str = ""
    email : str = ""
    options : str = ""
    cost : float = 0.0
    rating : int = 0 


def readfromfile():
    with open("orders.txt","r") as readfile:  #open orders.txt
        line=readfile.readline()
        counter=0
        orders=[order() for i in range(505)]  #create array of records for length of orders.txt
        while line:
            items=line.split(",")                  # separate file by commas
            orders[counter].orderNum = items[0]  #adds data from orders.txt to array of records
            orders[counter].date = items[1]
            orders[counter].email = items[2]
            orders[counter].options = items[3]
            orders[counter].cost = items[4]
            orders[counter].rating = items[5]
            counter += 1                     #increments counter by one to add to next position in array
        return orders



def findpositionofcustomer(orders):
    position = -1   # 2.1 Set position to -1
    index = 0   # 2.2 Set index to 0
    month = input("Please enter the month you want to search for")     # 2.3 Ask user to enter month to search for

    while (position == -1 and index < len(orders)):     # 2.4 While position is -1 and index is less than the length of the array
        if (orders[index].date[3:7]==month and orders[index].rating==5):     # 2.5 If current month is equal to searched month and current rating is 5 then
            position=index     # 2.6 Set position to index
        index+=1     # 2.8 Add 1 to index
    return position



def WriteDetailsOfWinningCustomer(orders,position):
    with open("winningCustomer.txt", "w") as writefile: #3.1 Open new file 'winningCustomer.txt'
        if (position >= 0): #3.2 if position is 0 or above then
            writefile.write(orders[position].orderNum + "," + orders[position].email + "," + str(orders[position].cost)) #3.3 Write winning order number, email and cost to 'winningCustomer.txt'
        else:
            writefile.write("No winner") #3.4 and 3.5 Write 'No winner' to 'winningCustomer.txt'

def countOption(orders):
    delivercount=0
    collectorcount=0
    for index in range (len(orders)):
        if (orders[index].option=="Delivery"):
            delivercount += 1

        elif (orders[index.option]=="Collection"):
            collectorcount += 1
    return delivercount, collectorcount

#main program

orders=readfromfile()
position=findpositionofcustomer(orders)