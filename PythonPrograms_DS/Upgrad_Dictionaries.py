
bio_data = {'Name':'bob marley','age':24,'job':'Assistant manager'}

print(bio_data)

names=bio_data['Name']
print(names)

#adding a key value pair
bio_data['Salary']=20000


print(bio_data)

# Create an existing dictionary
my_dict = {'key1': 'value1'}

# Add multiple key-value pairs using update()
my_dict.update({'key2': 42, 'key3': [1, 2, 3]})

# Print the dictionary
print(my_dict)
# Output: {'key1': 'value1', 'key2': 42, 'key3': [1, 2, 3]}


# NA is a default value 
names=bio_data.get('vamshi','NA')
print(names)

for values in bio_data.items():
    print(values)

print(len(my_dict))

# to pull out all the keys in a dictionary

print(bio_data.keys())

print(bio_data.values())