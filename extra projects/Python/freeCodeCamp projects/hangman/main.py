import random #Random to choose random word from list
from words import all_words #Importing 5000 words list
from PIL import Image #To show image of current phase

all_images = ["hangman/phase1.png", "hangman/phase2.png", "hangman/phase3.png", "hangman/phase4.png", "hangman/phase5.png", "hangman/phase6.png"] #Images of hangman phases
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_correct_word(all_words):
    user_word = random.choice(all_words)

    while "-" in user_word or " " in user_word:
        user_word = random.choice(all_words)

    return user_word.upper()


def main():
    word = get_correct_word(all_words=all_words)
    word_letters = set([i for i in word.upper()])
    updated_alphabet = set([i for i in alphabet])
    entered_letters = set()

    # Adding concept of lives
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # Showing used letters:
        if lives != 1:
            print(f"Letters you have already used are: {' | '.join(entered_letters)}\nYou have {lives} lives remaining!\n")
        else:
            print(f"Letters you have already used are: {' | '.join(entered_letters)}\nYou have {lives} live remaining!\n")

        # Showing remaining word
        remaining = [i if i in entered_letters else "_" for i in word]
        print(f"Your word is: {' '.join(remaining)}")
        
        # Input for letter
        user_letter = input("\nEnter character here: ").upper()

        if user_letter in updated_alphabet:  # Check if the input is a valid letter from the alphabet
            if user_letter in entered_letters:  # Letter is already entered
                print("\nYou have already entered that character")
            else:
                entered_letters.add(user_letter)  # Adding character to entered ones list
                if user_letter in word_letters:
                    word_letters.remove(user_letter)  # Word will have one character less
                    print("Correct letter!\n")
                else:
                    lives -=1 #Decrementing lives 
                    print("Wrong letter\n")

                    # Showing image
                    img = Image.open(all_images[-lives -1])

                    img.show()
        else:
            print("\nInvalid input. Please enter a letter from A to Z.")  # Input is not a valid letter
    
    #After the loop, user either guessed the word or had lives equal to 0
    if lives == 0:
        print(f"You lost, the word was: {word.lower()}")
    else:
        res = f"Congratulations! You guessed the word: {word.lower()}"
        print(f'\n{"-" * len(res)}')  #Adding design
        print(res)
        print(f'{"-" * len(res)}\n')

    print("Thanks for playing!\n")


main()

# Making game playable
decision = input("Play again? Y/N - ")

while decision == "Y" or decision == "y":
    main()
    decision = input("Play again? Y/N - ")