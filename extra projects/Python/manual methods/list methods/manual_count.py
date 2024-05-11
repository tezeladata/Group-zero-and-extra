def manual_count(iterable, element=None):
    if element is None:
        raise TypeError("manual_count() missing 1 required positional argument: 'element'")

    try:
        # Check if iterable is iterable
        _ = iter(iterable)
    except TypeError:
        raise ValueError("Input is not iterable")
    
    return len([i for i in iterable if i == element])