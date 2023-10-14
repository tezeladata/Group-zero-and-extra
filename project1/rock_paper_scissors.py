import random
while True:
    print("rock")
    print("paper")
    print("scissors")

    user = input("your choice: rock/paper/scissors: ")
    possible = ["rock", "paper", "scissors"]
    computer = random.choice(possible)

    print(f"\nYou chose {user}, computer chose {computer}.\n")

    if user==computer:
        print("tie game")
    elif user=="rock":
        if computer=="paper":
            print("computer wins")
        else:
            print("user wins")
    elif user=="paper":
        if computer=="rock":
            print("user wins")
        else:
            print("computer wins")
    elif user=="scissors":
        if computer=="paper":
            print("user wins")
        else:
            print("computer wins")
    else:
        print("wrong text")
    play_again = input("play again? yes/no: ")
    if play_again !="yes":
        break