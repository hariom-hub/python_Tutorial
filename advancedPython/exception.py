# let's learn and code exception handling in python
# payment = int(input("Enter the payment : "))
# try:
#     if (payment != 0):
#         print("transaction successful.")
# except Exception as e:
#     err = "payment amount cannot be zero."
#     print(err)
#
#
# print("---------------------------------")

num1 = int(input("Enter the divisor : "))
num2 = int(input("Enter the dividend : "))

if (num2 == 0):
    raise ZeroDivisionError("Sorry the dividend cannot be zero")
else:
    ans = int(num1 / num2)
    print(ans)
