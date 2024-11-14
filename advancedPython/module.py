def printNumber(n):
    print(n)


printNumber(10)


def printName():
    print("hello world")


'''suppose we are importing this file into another file for using the fucntionality of some block of code
then if we want that we don't want to include some block of code from the current file then
we can use __name__ = "__fileName__" to avoid extra code fuctionality.'''
if __name__ == "__main__":
    print("We are directly running this code.")
    printName()
    print(__name__)
