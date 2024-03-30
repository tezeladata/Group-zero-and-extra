def sort_by_len(arr):
    new_arr = sorted(arr, key=len) #ალაგებს სიგრძის მიხედვით
    new_arr = new_arr[::-1] # შებრუნება
    return new_arr


print(sort_by_len(["1", "1111", "11", "1111111"]))