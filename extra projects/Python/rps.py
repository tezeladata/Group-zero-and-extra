import random

def play_rock_paper_scissors():
    computer_score = 0
    user_score = 0
    play_again = "yes"

    while play_again.lower() == "yes":
        print("\nRock | Paper | Scissors\n")

        user = input("Your choice: rock / paper / scissors: ").capitalize()
        possible = ["Rock", "Paper", "Scissors"]
        computer = random.choice(possible)

        print(f"\nYou chose {user}\nComputer chose {computer}.\n")

        if user == computer:
            print("Tie game")
        elif user == "Rock":
            if computer == "Paper":
                print("Computer wins")
                computer_score += 1
            else:
                print("User wins")
                user_score += 1
        elif user == "Paper":
            if computer == "Rock":
                print("User wins")
                user_score += 1
            else:
                print("Computer wins")
                computer_score += 1
        elif user == "Scissors":
            if computer == "Paper":
                print("User wins")
                user_score += 1
            else:
                print("Computer wins")
                computer_score += 1
        else:
            print("Invalid choice")

        print(f"Scores are:\n| User - {user_score} |\n| Computer - {computer_score} |")
        play_again = input("\nPlay again? yes/no: ")

    print("Thanks for playing!")

# Call the function to play the game
play_rock_paper_scissors()