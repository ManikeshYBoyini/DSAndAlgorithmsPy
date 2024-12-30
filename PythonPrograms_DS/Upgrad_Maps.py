input_list= [1,2,3]
def cubes(num):
    return num**3

cube = list(map(cubes,input_list))
print(cube)


cube = list(map(lambda x:x**3, input_list))

print(cube)



input_list = ['San Jose', 'San Francisco', 'Santa Fe', 'Houston']

WordsWithS = (list(map(lambda word: 1 if word[0].lower()=='s' else 0,input_list)))

count = WordsWithS.count(1)

print(count)



from functools import reduce

#write your code here.
input_list=['All','you','have','to','fear','is','fear','itself']

output = reduce(lambda x,y : x+" "+y,input_list)

print(output)

D = {1:['Raj', 22], 2:['Simran', 21], 3:['Rahul', 40]}
for val in D:
     print(val)
