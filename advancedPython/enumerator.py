# nums = [10, 20, 30, 40]
# index = 0
# for item in nums:
#     print(f"{item} is present at index {index}")
#     index += 1
# let's do the same thing with enumerator
# mylist = [10,20,30,40]
# squaredList = [i*i for i in mylist]
# print(squaredList)


num = int(input("Enter a number : "))
numslist = list()
for x in range(1, 11):
    numslist.append(num * x)

print(numslist)

with open("table.txt","a") as table:
    table.write(str(numslist)+"\n")
