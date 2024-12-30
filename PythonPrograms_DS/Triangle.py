def Triangle(n):
    k=n-1
    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")

        k=k-1
        
        for r in range(0,i+1):
            print("* ",end="")
        
        print("\r")


num= int(input("Enter the row count for triangle\n"))
Triangle(num)