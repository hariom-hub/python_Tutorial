# def main():
#     a = True
#     return a

# print(main())

# #type casting in python
# a = 99.3
# print(type(a))
# b = str(a)
# print(type(b))
# print(b)
# c = "codewithhariom"

# def sum():
#     n1 = int(input("Enter the first number"))
#     n2 = int(input("Enter the second number"))
#     sum = n1 + n2
#     return sum

# print("sum is : ",sum())

# print("harry"+ "coder")

# i = 0
# while i < 6 : 
#     i = i + 1
#     if(i==5):
#         print(i)

# def factorial(n): 
#     if(n==0):
#         return 1
#     else :
#         return n * factorial(n-1)
    
# print("factorial is :",factorial(5))

# for x in range(0,5):
#     for y in range(0,x):
#         print("*",end=" ")
#     print()

matrix = [
    [1,2,3,4,11],
    [5,6,7,8,1],
    [9,10,11,12],
    [13,14,15,16],
    [17,18,19,20]
]

# hariom = ["men","strong","passionate"]
# print(len(hariom))
# print(len(matrix[0]))
# print(len(matrix))
# print(matrix[0][1] % matrix[0][2])

# num = int(input("Enter a number"))
# print(type(num))

# a = 34
# b = 80
# if(a>b):
#     print("a is greater than b")
# else:
#     print("b is greater than a")
# n = int(input("Enter a number : "))
# #cube
# cube = n*n*n
# print("cube of ",n, "is : ",cube)

#average of three numbers
# n1 = int(input("Enter number 1 : "))
# n2 = int(input("Enter number 2 : "))
# n3 = int(input("Enter number 3 : "))
# avg = float(n1+n2+n3) / 3
# print(avg)
# number = int(input("Enter a number : "))
# print(number**2)
import randfacts as rf
fact = rf.get_fact()
print(fact)
string = "hariomsinghthakur"
substr = string[0:6]
print(substr)