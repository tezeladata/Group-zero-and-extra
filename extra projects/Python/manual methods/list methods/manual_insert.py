def manual_insert(collection, element, index):
    if index < 0:
        index = len(collection) + index

    try:
        return collection[:index] + [element] + collection[index:]
    except TypeError:
        raise TypeError("insert expected 2 arguments, got 0")

print(manual_insert([1, 2, 3, 4, 5], 10, 0))