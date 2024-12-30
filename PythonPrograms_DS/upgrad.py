n = 4
[print(a**2) for a in range(1,n+1)]


wordslist=[]
vowel = ['a', 'e', 'i', 'o', 'u']
words = ['wood','old','apple','big','item','euphoria']
wordslist = [word for word in words if word[0].lower() in vowel]

print(wordslist)