# walrus operator
if (n := len([10, 20, 30, 40, 50])) > 4:
    print(f"list is too long")

n: int = 5
name: str = "harry"


def sum(a: int, b: int) -> int:
    return a + b


student1 = {
    "name" : "hariom",
    "age" : 20,
    "height" : 5.8
}

student2 = {
    "name" : "ritansh",
    "age" : 21,
    "height" : 5.7
}
#let's merge dictionaries
finaldict = student1|student2
print(finaldict)