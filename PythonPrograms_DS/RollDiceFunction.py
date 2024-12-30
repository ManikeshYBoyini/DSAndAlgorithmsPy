import random

def RollDice():
    return random.randint(1,6)+random.randint(1,6)

def main():
    player1= input("Enter the first player name:\n")
    player2=input("Enter the second player name:\n")

    roll1= RollDice();
    roll2=RollDice();

    print(player1,' rolled: ',roll1)
    print(player2,' rolled ',roll2)

    if roll2>roll1:
        print("player2 wins")
    elif roll1>roll2:
        print("player1 wins")
    else:
        print("you tie")


main()
