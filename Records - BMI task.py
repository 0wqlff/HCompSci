from dataclasses import dataclass
@dataclass
class person():
    name : str = ''
    mark : int = 0
    bmi : float = 0.0

BMIdetails = [person() for index in range(40)]

BMIdetails[0].height = 1.75
BMIdetails[0].weight = 70.5
BMIdetails[0].bmi = BMIdetails[0].weight / (BMIdetails[0].height**2)

BMIdetails[0].height = 1.62
BMIdetails[0].weight = 55.8
BMIdetails[0].bmi = BMIdetails[0].weight / (BMIdetails[0].height**2)

BMIdetails[0].height = 1.88
BMIdetails[0].weight = 95.2
BMIdetails[0].bmi = BMIdetails[0].weight / (BMIdetails[0].height**2)

BMIdetails[0].height = 1.70
BMIdetails[0].weight = 
BMIdetails[0].bmi = BMIdetails[0].weight / (BMIdetails[0].height**2)
