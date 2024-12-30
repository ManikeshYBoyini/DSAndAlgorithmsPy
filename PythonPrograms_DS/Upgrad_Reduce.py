from functools import reduce

n = 10
factorial = reduce(lambda x,y : 1 if x==0 or x==1 else x*y, reversed(range(1,n+1)) )
print(factorial)