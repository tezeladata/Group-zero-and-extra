def main():
    # Starter func
    def greeting():
        print("Hello, this code converts natural text to nato language text.")
        print("After your input, you will get translated text\n")

    greeting()

    # User input:
    words = input("Enter text here: ")

    # Did not use library, just dict
    d = {
        'A': 'Alfa',  'B': 'Bravo',   'C': 'Charlie',
        'D': 'Delta',  'E': 'Echo',    'F': 'Foxtrot',
        'G': 'Golf',   'H': 'Hotel',   'I': 'India',
        'J': 'Juliett','K': 'Kilo',    'L': 'Lima',
        'M': 'Mike',   'N': 'November','O': 'Oscar',
        'P': 'Papa',   'Q': 'Quebec',  'R': 'Romeo',
        'S': 'Sierra', 'T': 'Tango',   'U': 'Uniform',
        'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
        'Y': 'Yankee', 'Z': 'Zulu'
    }
    
    res = " ".join([d[char] if char in d else char for char in words.upper() if char in d or char in ",.!?"])

    print(f"After translating, your text looks like: \n{res}")

main()