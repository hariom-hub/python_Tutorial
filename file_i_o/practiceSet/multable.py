# def table():
#     nums = []  # nums list to store the nums
#     # taking input
#
#     n = int(input("Enter the number : "))
#     for x in range(1, 11):
#         nums.append(n * x)
#         with open("multiply.txt", "a") as mul:
#             mul.write(f"\n printing the table of {n}\n{str(nums)}")
#
#
# table()

def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)


for i in range(1, 21):
    generateTable(i)
