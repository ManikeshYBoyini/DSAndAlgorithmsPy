lst=[]

lst.append(4)
lst.append("work")
lst.append(True)

print(lst)

lst.pop(1)

print(lst)

s=set()
s.add(1)
s.add(2)
s.add("work")
s.add(2)

print(s)

s.remove("work")
c= s.copy()

print(s)
print("copied set" , c)


tpl=()
tpl= tpl+ (12,23,34)

print(tpl)

dkey ={}
dkey[3]="three"
dkey[4]="four"
dkey[4]="five"

print(dkey)

del dkey[3]

print(dkey)