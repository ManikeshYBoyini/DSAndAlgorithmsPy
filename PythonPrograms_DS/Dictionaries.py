acronyms={}

# add keyvalue pairs
acronyms={'LOL':'Laugh out loud','IDK':'I Dont know','BTW':'By The Way','TBH':'To Be Honest'}

print(acronyms)

#Update a value of the key
acronyms['LOL']= 'laugh out low'

print(acronyms)

# delete a key value pair in a dictionary
del acronyms['LOL']
print(acronyms)

sentence = 'IDK'+' what happened ' +'TBH'
translation= acronyms.get('IDK')+' What happened '+acronyms.get('TBH')

print('sentence: ', sentence,' , Translation: ',translation)

#If we use forloop over a dictionary if will print only the keys

for i in acronyms:
    print(i)


for name, value in acronyms.items():
    print(name,': ',value)