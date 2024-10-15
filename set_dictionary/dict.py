# let's learn about dictionaries and sets

data = {

    "name" : "hariom",
     "age" : 20,
    "height" : 5.7,
    "number" : 9303326686,
    "hobby" : "swimming"
}
print(type(data))
print(data)
print(data["age"])
print(data["number"])
data.update({"height" : 6.3})
print(data)
print(data.values())
print(data.keys())
print(data.items())
data.pop("hobby")
print(data.items())
print(data.pop("age"))
print(data.items())

