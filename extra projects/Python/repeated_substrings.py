def f(s):
    length = len(s)

    def can_construct_by_repeating(t):
        return t * (length // len(t)) == s

    for i in range(1, length + 1):
        if length % i == 0:
            t = s[:i]
            if can_construct_by_repeating(t):
                return (t, length // i)

    return (s, 1)

print(f(s=input("Enter text to find it's most repeated substring: ")))