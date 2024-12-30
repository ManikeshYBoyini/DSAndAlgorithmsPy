total =0
expenses=[]

for i in range(7):
    expenses.append(float(input("please enter the expense\n")))

total = sum(expenses)

print("your total expenses are $",sum,sep='')