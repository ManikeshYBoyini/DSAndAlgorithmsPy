num= input("Enter the string\n")

#print("Original string is "+str(num))

reverseNum= num[::-1]

result=num==reverseNum

if result==True: 
    print(num + " is a palindrome")
else:
    print(num +" is not a palindrome")