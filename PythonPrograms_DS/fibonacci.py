LastNum= int(input("Please enter the count of the fibonacci\n"))

n1=0
n2=1

print("Fibonacci series: ",n1,n2, end=" ")

for num in range(LastNum):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3, end=" ")
                   
