def manual_list(to_list = None):
    if to_list is None:
        return []
    elif isinstance(to_list, list):
        return to_list
    else:
        try:
            return [i for i in to_list]
        except TypeError:
            raise TypeError("Input is not iterable")