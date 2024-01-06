def reverse_words(text):
    text=list(text.split(" "))
    new=""
    for element in text:
        new+=element[::-1]
        new+=" "
    return new.strip(" ")
print(reverse_words(text=input("Enter text: ")))