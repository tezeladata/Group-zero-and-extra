def manual_map(function, iterable):
    try:
        iter(iterable)
    except TypeError:
        raise TypeError("Input not iterable")
    
    return [function(i) for i in iterable]

def map_func(value):
    return value**2