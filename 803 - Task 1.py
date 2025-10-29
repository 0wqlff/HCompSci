# #modular programming

# def displayNames(nameList):
#   print("Current list")
#   for loop in range(len(nameList)):
#     print("Forename",nameList[loop][0])
#     print("Surname",nameList[loop][1])

# nameList = [["Matthew","Reid"]]
# numNames = int(input("How many names do you wish to add?"))
# for names in range(numNames):
#   newForename = str(input("Please enter a forename"))
#   newSurname = str(input("Please enter a surname"))
#   nameList.append([newForename, newSurname])

# displayNames(nameList)

# Predict and Run - Task 2

def displayScoreData(scores):
  average = sum(scores)/len(scores)
  print("Average score:",round(average,1))
  print("Scores ranged from:")
  print(min(scores),"to",max(scores))

# Main program
scores = [4,6,8,5,6,3,5,9,10,2,4,6,3,5]
displayScoreData(scores)
scores = [50,51,52,56,59,68]
displayScoreData(scores)