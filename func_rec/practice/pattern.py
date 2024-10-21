def printPattern(rows):
    for x in range(rows + 1, 1, -1):
        for y in range(1, x):
            print("*", end=" ")
        print(" ")


rows = int(input("Enter the number of rows : "))
printPattern(rows)
