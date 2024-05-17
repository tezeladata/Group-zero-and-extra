def madlibs():
    print("\nHello this is madlibs game!\n")

    madlibs_list = ["In the heart of the", "city, the", "musician decided to", "with the elegance of"]

    noun = input("Enter noun: ")
    adjective = input("Enter adjective: ")
    verb = input("Enter verb: ")
    famous_person = input("Enter famous person: ")

    user_words = [noun, adjective, verb, famous_person]

    for i in range(1, 8, 2):
        madlibs_list.insert(i, user_words[i // 2])

    return f"Your sentence with words - {' '.join(user_words)} is:\n{' '.join(madlibs_list)}"

print(madlibs())