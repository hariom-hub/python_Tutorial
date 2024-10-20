# let's get started with functions and recursion in pythion
from math import factorial


def Sum(a, b):
    return a + b


# print(Sum(10,20))


def avg(a, b, c):
    return float((a + b + c) / 3)


# print(avg(13,17,34))

def primeNum():
    n = int(input("Enter a number : "))

    if n <= 1:
        print(f"{n} is not a prime number.")
        return
    i = 2

    while i < n:
        if n % i == 0:
            print(f"{n} is not a prime number.")
            return
        i += 1
    print(f"{n} is a prime number.")


# primeNum()

# check palindrome

def palindromeStr():
    name = input("Enter a name : ")
    i = 0
    j = len(name) - 1
    while i <= j:
        if name[i] != name[j]:
            print(f"{name} is not a palindrome string.")
            return
        i += 1
        j -= 1
    print(f"{name} is a palindrome string.")


# palindromeStr()

def Fact():
    n = int(input("enter a number : "))
    fact = 1
    for x in range(1, n + 1, 1):
        fact = fact * x

    print(f"factorial of {n} is : {fact}")

# Fact()

def greet():

    Str = input("Enter a name : ")
    greeting = f"hello {Str}"
    return greeting

print(greet())