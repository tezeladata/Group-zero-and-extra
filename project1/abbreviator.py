print("Hello, this code abbreviates your name")
def abbreviation(name):
    first=name[0]
    for letter in range(len(name)):
        if name[letter]==" ":
            last=name[letter+1]
    print ("Abbreviation for name:", name, "is:", (first.upper() + "." + last.upper()))
    print("Thanks for attention!")
abbreviation(name=input("Enter your name: "))