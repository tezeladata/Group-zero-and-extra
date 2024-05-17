import random

sentences = [
    ["Georgia, nestled at the crossroads of Europe and _, boasts a _ tapestry of _ and culture.", ["Asia", "rich", "history"]],

    ["Tbilisi, the capital of _, is a vibrant city characterized by its eclectic _, lively _, and thermal baths.", ["Georgia", "architecture", "markets"]],

    ["The _ Mountains, which dominate much of Georgia's _, offer breathtaking _ and opportunities for outdoor adventure.", ["Caucasus", "landscape", "scenery"]],

    ["Georgian _, known for its flavorful dishes such as _ (cheese-filled bread) and _ (dumplings), is a highlight for visitors to the country.", ["cuisine", "khachapuri", "khinkali"]],

    ["Georgia's ancient monasteries and churches, including the UNESCO World Heritage Site of Gelati _, reflect the _ deep religious _.", ["Monastery", "country's", "heritage"]]
]

def guesser():
    print("Hello, this is a word guessing game. You have to fill in the blanks.")

    selected = random.choice(sentences)
    sentence = selected[0]
    correct_words = selected[1]
    remaining = 5

    print(f"\nYour sentence is: \n\n| {sentence} |\n")

    for i in range(len(correct_words)):
        while True:
            user_word = input(f"Enter word for blank {i+1}: ")

            if user_word.strip().lower() == correct_words[i].lower():
                print("\nCorrect guess! Your sentence now looks like:\n\n")
                sentence = sentence.replace('_', user_word, 1)
                print(f"| {sentence} |\n")
                break
            else:
                remaining -= 1

                print("\nWrong guess! Your sentence now looks like:\n")

                if remaining == 0:
                    print("You lost!")
                    return

                print(f"Your guess is wrong. {remaining} tries remaining.\n")

    print("Congratulations! You filled in all the blanks correctly!")


guesser()