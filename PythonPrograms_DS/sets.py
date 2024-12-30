student1 =set(['A','A','B','C','B','D','D'])

student2 =set(['E','F','G','H','B','D','C'])

print(sorted(student1))

print(sorted(student2))

print("intersection", student1.intersection(student2)) # common elements 
print("difference", student1.difference(student2)) # student1 - student2
print("symmetric difference",student1.symmetric_difference(student2)) # not common elements in both sets
print("union",student1.union(student2))  # student1 + student2



C= [2, 5, 9, 12, 13, 15, 16, 17, 18, 19]
F = [2, 4, 5, 6, 7, 9, 13, 16]
H = [1, 2, 5, 9, 10, 11, 12, 13, 15]

cset = set(C)
fset=set(F)
hset=set(H)
aset=set(range(1,21))

chandh = sorted(cset.intersection(fset).intersection(hset))
candhbutnoth = sorted((cset.intersection(fset)).difference(hset))
twosports = sorted((cset.union(fset).union(hset)).difference((cset.symmetric_difference(fset).symmetric_difference(hset))))
anysports = sorted(aset.difference(cset.union(fset).union(hset)))


print(chandh)
print(candhbutnoth)
print(twosports)
print(anysports)