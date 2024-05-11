def manual_filter(function, iterable):
    try:
        iter(iterable)
    except TypeError:
        raise TypeError("Input not iterable")
    
    return [i for i in iterable if function(i)]

def filt_func(value):
    return value%2==0