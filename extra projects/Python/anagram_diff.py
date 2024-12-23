def anagram_difference(w1, w2):
    def add_counts(st, ls):
        for char in st:
            ls[ord(char) - 97] += 1

    count1, count2 = [0] * 26, [0] * 26

    add_counts(w1, count1)
    add_counts(w2, count2)

    result = 0
    for i in range(26): result += abs(count1[i] - count2[i])

    return result