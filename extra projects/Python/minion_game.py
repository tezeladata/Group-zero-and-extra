def minion_game(string):
    stuart_score = 0
    kevin_score = 0
    
    vowels = "AEIOU"

    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i

    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif stuart_score < kevin_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")