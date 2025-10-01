def intructo():
    print("Welcome to your temperature converter!!!")
    print("Enter a temperature in Celsius or Fahrenheit and we will convert it for you!! Simple as that!")
    print("========================================================================================================")
    print("========================================================================================================")

def accio():
    print("Pretty please may you kindly provide us with the information relating to the name of your chosen unit of temperature,")
    print("if it is not too much work, of course, THANK YOU!!")
    unit=input("Unit: ")
    print("AND NOW, for the value of such temperature to be provided.")
    value=int(input("Value: "))
    return unit, value 

def validito():
    