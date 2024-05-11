def manual_pop(iterable, index = None):
    if index is None:
        index = len(iterable) - 1

    if index < 0:
        index = len(iterable) + index

    return [iterable[i] for i in range(len(iterable)) if i != index]