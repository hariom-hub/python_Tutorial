cube = lambda x:x*x*x
print(cube(10))
print(cube(200))

names = ["hariom","singh","thakur"]
fullname = " ".join(names)
print(fullname)

nums = [1,2,3,4,5]
sq_nums = lambda x:x*x

sq_list = map(sq_nums,nums)
print(list(sq_list))