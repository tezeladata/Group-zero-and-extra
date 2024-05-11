def manual_max(iterable):
    try:
        iter(iterable)
    except TypeError:
        raise TypeError("Input not iterable")
    
    return sorted(iterable)[-1]

def manual_max2(iterable):
    try:
        iter(iterable)
    except TypeError:
        raise TypeError("Input not iterable")
    
    max = iterable[0]
    for num in iterable:
        if num > max:
            max = num

    return max