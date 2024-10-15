# let's learn about sets in python

s1 = {10,20,30,60}
s2 = {40,50,60}
print(type(s1))
print(type(s2))
print(s1.union(s2))
print(s2.union(s1))
print(s1.intersection(s2))
print(s2.intersection(s1))
#methods on sets
s1.add(50)
s2.remove(50)
print(s1)
print(s2)
print(s1.pop())
print(s1)
subset_s1 = {20,30}
print(subset_s1.issubset(s1))
unionSet = s1.union(s2)
print(unionSet)