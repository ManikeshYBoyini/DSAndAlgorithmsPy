var1= ('Monty python', 'Formula1',1,True)

print(var1)
print(var1[2])
print(var1[:-1])

var2=list(var1)

var2.append('This is a list now')

[print(x) for x in var2]

var1[1]="changed"
print(var1)



# upgrad question below

input_tuple = ('Monty Python', 'British', 1969)

# Write your code here
list_str=list(input_tuple)
list_str.append('Python')
tuple_2 = tuple(list_str)
# Make sure to name the final tuple 'tuple_2'
print(tuple_2)