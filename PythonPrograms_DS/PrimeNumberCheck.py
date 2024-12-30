num = int(input("Enter the number\n"))

if num>0:
    for n in range(2,int(num/2)+1):
        if(num%n)==0:
            print(str(num) +" is not a prime number")
            break
    else:
        print(str(num) +" is a prime number")             

else:
    print(str(num) + " is not a prime number")