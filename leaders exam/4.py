def shortest_word(arr):
    new_arr = sorted(arr, key=len) #ალაგებს სიგრძის მიხედვით
    return new_arr[0] #აბრუნებს უმცირესს


print(shortest_word(["goal", "oriented", "academy", "goa", "goabest"]))
print(shortest_word(["Mercedes", "gatrinolebuli e46 faramogebuli", "tevzadze e34", "hoonigan"]))