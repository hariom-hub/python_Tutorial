i = 0
while i < 5:
    print("hello world")
    i += 1

names = ["hariom", True, 1, 14.3, "aks university"]

for x in range(len(names)):
    print(names[x])

fruits = (1, 2, 3, 4, 50)
for x in range(len(fruits)):
    print(fruits[x])

Dict = {

    "name": "gadha",
    "age": 20,
    "height": 5.8
}

print(Dict.keys())
print(Dict.get("name"))

print("keys in the dictionary Dict")
for key in Dict.keys():
    print(key)

for vals in Dict.values():
    print(vals)

for key, vals in Dict.items():
    print(f"{key}:{vals}")

name = "HariomSinghThakur"
for st in name:
    print(st)

# print table of 10

# n = int(input("Enter a number : "))
# i = n
# while i >= 1:
#     print(i * n)
#     i = i - 1

# num = int(input("Enter a number : "))
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")


# fact = 1
# i = 1
# n = int(input("Enter a number : "))
# while i<=n:
#     fact = fact * i
#     i += 1
#
# print(fact)


n = int(input("Enter a number : "))
fact = 1
for i in range(1,n+1):
    fact = fact * i

print(fact)
