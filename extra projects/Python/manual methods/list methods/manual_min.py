def manual_min(iterable):
    try:
        iter(iterable)
    except TypeError:
        raise TypeError("Input not iterable")
    
    return sorted(iterable)[0]

def manual_min2(iterable):
    try:
        iter(iterable)
    except TypeError:
        raise TypeError("Input not iterable")
    
    min = iterable[0]
    for num in iterable:
        if num < min:
            min = num

    return min