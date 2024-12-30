import random


computer_choice=random.choice(['scissors','rock','paper'])
user_choice=input('Do you want - rock, paper, or scissors?\n' )

computer_choice=computer_choice.lower()
user_choice=user_choice.lower()

if computer_choice==user_choice:
    print("TIE, The computer had "+str(computer_choice))
elif user_choice=='rock' and computer_choice=='scissors':
    print("You Win, The computer had "+str(computer_choice))
elif user_choice=='scissors' and computer_choice=='paper':
    print("You Win, The computer had "+str(computer_choice))
elif user_choice=='paper' and computer_choice=='rock':
    print("You Win, The computer had "+str(computer_choice))
else:
    print("You lose ;( computer wins :D. The computer had "+str(computer_choice))