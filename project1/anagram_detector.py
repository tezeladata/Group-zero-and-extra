print("Hello, this is anagram detector!")
print("Note that anagrams are case insensitive.")
def detector(str1, str2):
    if sorted(str1.lower())==sorted(str2.lower()):
        return "Anagram detected!"
    else:
        return "Not anagram!"
print(detector(str1=input("Enter first word: "), str2=input("Enter second word: ")))