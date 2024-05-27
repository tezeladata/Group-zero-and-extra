def insertion_sort(user_arr):
    # Inner function
    def inner_func(cabinet,to_insert):
        check_location = len(cabinet) - 1
        insert_location = 0

        # Loop to find correct location
        while(check_location >= 0):
            if to_insert > cabinet[check_location]:
                insert_location = check_location + 1
                check_location = - 1
            check_location = check_location - 1

        # After finding correct location, we can use as index with insert function
        cabinet.insert(insert_location,to_insert)
        return cabinet

    new_array = []

    # While original array is not sorted, we use inner_func to add numbers to correct places
    while len(user_arr) > 0:
        to_insert = user_arr.pop(0)
        new_array = inner_func(new_array, to_insert)

    return new_array

def generate_arr():
    return [int(input("Enter number: ")) for _ in range(int(input("How many elements do you want to have in your array: ")))]

print(f"Your result after insertion sort is: {insertion_sort(generate_arr())}")