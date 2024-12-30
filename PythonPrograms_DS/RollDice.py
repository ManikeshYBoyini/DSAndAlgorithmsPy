import random

roll = random.randint(1,6)
# print("The computer rolled a "+str(roll))

guess = int(input("Please enter the guess number\n"))

if guess==roll:
    print("your guess is correct "+ str(roll))
else:
    print("wrong guess,, the computer rolled:  "+str(roll))