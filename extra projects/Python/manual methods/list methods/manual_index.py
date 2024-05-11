def manual_index(iterable, element = None, start = 0, end = None):
    if element is None:
        raise TypeError("index expected at least 1 argument, got 0")
    
    if end is None:
        end = len(iterable)
    
    ind_list = [i for i in range(start, end) if iterable[i] == element]

    if ind_list:
        return ind_list[0]
    return -1