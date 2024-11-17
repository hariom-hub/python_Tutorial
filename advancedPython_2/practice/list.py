NUMS = [1,3,35,8325,100,20,45,89,76,82]
div_5 = lambda x:x%5==0
ans = filter(div_5,NUMS)
print(list(ans))
#here map function will return true or false whrereas filter will return the values following the constraint function defined
