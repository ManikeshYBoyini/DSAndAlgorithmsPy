from os import sep


expenses=[10.50,6,8,23,13.50,12]

summ =0

for expense in expenses:
    summ=summ+expense

if summ>0:
    print("you spent $",(summ)," on lunch this week",sep='')


total = sum(expenses)

print(str(total))





