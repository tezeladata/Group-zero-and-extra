print("This code counts you letter from your string.")
def count(word):
    result=[]
    for i in word:
        occurences=(i, word.count(i))
        if occurences not in result:
            result.append(occurences)
    return "Ordered count of letters in {} is: \n {}".format(word, result)
print(count(word=input("Enter word: ")))