import math
class calculator:
    def __init__(self, num):
        self.num = num
        square = num * num
        cube = num * num * num
        squareRoot = math.sqrt(num)
        print(f"square of {num} = {square}")
        print(f"cube of {num} = {cube}")
        print(f"squareroot of {num} = {squareRoot}")


number = int(input("Enter a valid number : "))
obj = calculator(number)
