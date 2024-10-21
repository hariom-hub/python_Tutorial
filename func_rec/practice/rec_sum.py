def recSum(num):
    if num == 0:
        return 0
    Sum = num + recSum(num - 1)
    return Sum


n = int(input("Enter a number : "))
print(f"sum is : ",recSum(n))
