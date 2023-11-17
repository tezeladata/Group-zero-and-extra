print("Hello, this code counts vowels!")
def vowel_counter(text):
    vowels="a", "e", "i", "o", "u", "A", "E", "I", "O", "U"
    counter=0
    for i in range(len(text)):
        if text[i] in vowels:
            counter+=1
    print("This code counted {} vowels in yout text.".format(counter))
vowel_counter(text=input("Enter text you want vowels be counted for: "))
print("Thanks for attention!")