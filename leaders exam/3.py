def to_word(arr):
    new_arr= [chr(x) for x in arr]  # აქ გარდაიქმნება და განიხილავს მთლიან სიას
    return "".join(new_arr) # სთრინგად



print(to_word([103, 111, 97]))
print(to_word([103, 111, 97, 97, 99, 97, 100, 101, 109, 121]))