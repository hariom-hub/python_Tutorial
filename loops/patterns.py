#printing rectangle pattern
# rows = int(input("Enter the number of rows : "))
# cols = int(input("Enter the number of cols : "))
#
# for x in range(1, rows + 1):
#     for y in range(1, cols + 1):
#         if (x == 1 or x == rows) or (y == 1 or y == cols):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print(" ")


#printing right triangle pattern

# n = int(input("Enter the number of rows : "))
# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print("*",end = " ")
#     print(" ")

#printing pyramid patterns

rows = int(input("Enter the number of rows : "))
for x in range(1,rows+1):
    print(" "*(rows-x),end = " ")
    print(" * "*(2*x-1),end = " ")
    print(" ")
