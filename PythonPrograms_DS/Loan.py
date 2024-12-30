money_owed= float(input("How much money do you owe, in rupees?\n"))
interestPerAnnum = float(input("What is the annual percentage rate?\n"))
payment= float(input("What will be your monthly payment be, in rupees?\n"))
months=int(input("How many months do you want to see results?\n"))

monthly_rate= interestPerAnnum/100/12

for i in range(months):
    if(money_owed-payment<0):
        print("The last payment is ",money_owed)
        print("You paid off the loan in ",i-1,"months")
        break

    interest_paid= monthly_rate*money_owed;

    money_owed= money_owed+interest_paid

    money_owed= money_owed-payment;

    print("Paid ", payment,"of which ", interest_paid, "is the interest", end=' ')
    print("The total amount owed is ",money_owed)
  