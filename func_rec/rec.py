# recursion using python
import random
from random import choice
from urllib.parse import uses_relative


# factorial program

def Fact(n):
    if n == 0 or n == 1:
        return 1
    fact = n * Fact(n - 1)
    return fact


# num = int(input("Enter a number : "))
# print(f"factorial of {num} is : {Fact(num)}")

# fibonacci series

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


# num = int(input("Enter a number: "))
# print(fib(num))

def takeInput():
    num = int(input("Enter a number : "))
    return num


def generateRandNum():
    lowerLimit = int(input("Enter the lower limit : "))
    upperLimit = int(input("Enter the upper limit : "))
    randNum = random.randint(lowerLimit, upperLimit)
    return randNum


def start():
    print("LET'S START THE GAME ")
    userNum = takeInput()
    randNum = generateRandNum()
    if userNum == randNum:
        print("Hurray! you got it")
    else:
        print("Sorry number didn't matched.")
        choice = input("Want to quit ?(yes or no) : ")
        if choice == "yes":
            print("---------Game Over-------------")
            return
        else:
            print("Try again")
            start()


start()
