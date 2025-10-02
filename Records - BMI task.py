from dataclasses import dataclass
@dataclass
class person():
    name : str = ''
    mark : int = 0
    bmi : float = 0.0

BMIdetails = [person() for index in range(40)]

BMIdetails