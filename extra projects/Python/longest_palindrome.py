def longest_palindrome(s):
    def is_palindrome(sub):
        return sub == sub[::-1]

    longest_length = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(s[i:j]):
                longest_length = max(longest_length, j - i)
    return longest_length