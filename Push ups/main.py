# მონაცემების შეტანა
starting_list = []

def sort_users(name, x, y):
    starting_list.append([name, x, y])

sort_users("abashidze", 65, 44)
sort_users("koxreidze", 42, 65)
sort_users("varadashvili", 56, 26)
sort_users("xucishvili", 60, 26)
sort_users("yifshidze", 38, 24)
sort_users("gio xaniashvili", 29, 70)
sort_users("svanidze", 77, 51)
sort_users("girgvliani", 56,41)
sort_users("akolashvili", 32,21)
sort_users("mardaleishvili", 34,30)
sort_users("gabriel xaniashvili", 31,100)
sort_users("maisuradze", 58,31)
sort_users("wawiashvili", 50, 64)
sort_users("dolidze", 78,42)
sort_users("burchuladze", 36, 16)
sort_users("asanashvili", 70, 41)
sort_users("samushia", 63, 40)
sort_users("basharuli", 43, 41)
sort_users("janeza", 95, 25)


# მახასიათებლის გამოთვლა
sorted_list = []
def sort_data(list):
    sorted_list.append([list[0], (list[2] * list[1] / 20)])

for i in range(len(starting_list)):
    sort_data(starting_list[i])


# სიის დასორტირება
sorted_list.sort(key=lambda x: x[1], reverse=True)


# dict-ის სახით დაბეჭვდა
user_dict = dict()

for list in sorted_list:
    user_dict[list[0]] = list[1]

print(user_dict)