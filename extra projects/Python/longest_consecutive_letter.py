def longest_repetition(chars):
    if not chars: return ('', 0)
    all, score = [], 1
    for i in range(len(chars)-1):
        if chars[i] == chars[i+1]: score += 1
        else:
            all.append([chars[i], score])
            score = 1
    all.append([chars[-1], score])
    all.sort(key = lambda x: x[1], reverse=True)
    return (all[0][0], all[0][1])