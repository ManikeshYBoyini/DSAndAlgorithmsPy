acronyms = []

acronyms.append('LOL')
acronyms.append('ROFL')
acronyms.append('IDK')
acronyms.append('SMH')
acronyms.append('TBH')
acronyms.append('BFN')

print(acronyms)

acronyms.reverse()

print(acronyms)

acronyms.remove('LOL')

acronyms.insert(2,'LOLL')

print(acronyms[1])

print(acronyms)

acronyms.pop()

print(acronyms)

wordTobechecked= input("Enter the acronym you want to check\n")

if wordTobechecked in acronyms:
    print(wordTobechecked + " is available")
else:
    print(wordTobechecked + " is not available")