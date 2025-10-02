i=1
def go():
    from dataclasses import dataclass
    @dataclass
    class person():
        height : float = 0.0
        weight : float = 0.0
        bmi : float = 0.0

    BMIdetails = [person() for i in range(5)]

    def get_values():
        heights=int(input("What is your height? "))
        weights=int(input("What is your weight? "))
        return heights, weights

    def calculate():
        for i in range(5):
            BMIdetails[i].height, BMIdetails[i].weight = get_values()
            BMIdetails[i].bmi = BMIdetails[i].weight/(BMIdetails[i].height**2)

    def display():
        for i in range(5):
            print(BMIdetails[i])

    calculate()
    display()
while i!=0:
    go()



