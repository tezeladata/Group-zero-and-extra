# მონაცემების შეტანა
starting_list = []

def sort_users(name, x, y):
    starting_list.append([name, x, y])

sort_users("ალექსანდრე ჩიხლაძე", 37, 0)
sort_users("ნუკი გაგნიძე", 40, 0)
sort_users("ზურა ცინცაძე", 45, 0)
sort_users("ლუკა გორგაძე", 45, 0)
sort_users("ერეკლე ნაპირელი", 47, 0)
sort_users("გიორგი სამსონიძე", 48, 0)
sort_users("საბა ფუთურიძე", 48, 0)
sort_users("საბა ისაკაძე", 50, 0)
sort_users("მათე ჩუბინიძე", 50, 0)
sort_users("გიგა კოჩალიძე", 51, 0)
sort_users("ნიკოლოზ გიგოშვილი", 53, 0)
sort_users("გაბრიელ გვასალია", 53, 0)
sort_users("ალექსი ბახტაძე", 53, 0)
sort_users("თორნიკე ბერიძე ", 54, 0)
sort_users("დავით ტუღუში", 55, 0)
sort_users("ჟანა გაბლია", 55, 0)
sort_users("ანრი გიუნაშვილი", 55, 0)
sort_users("ნიკოლოზი დობორჯგინიძე", 55, 0)
sort_users("ლუკა მერუმოვი", 55, 0)
sort_users("გიორგი ვარადაშვილი ", 56, 0)
sort_users("ალექსანდრე რევია", 58, 0)
sort_users("ლუკა დგებუაძე ", 58, 0)
sort_users("ლუკა ჭანიშვილი ", 58, 0)
sort_users("ნიკოლოზ ტეფნაძე", 58, 0)
sort_users("ლევან სამსონიძე", 60, 0)
sort_users("გიგა ხუციᲨვილი", 60, 0)
sort_users("ალექსანდრე შალიკაშვილი", 60, 0)
sort_users("ცოტნე გულბანი", 60, 0)
sort_users("ucha khuberishvili", 62, 0)
sort_users("თორნიკე ნებიერიძე", 63, 0)
sort_users("თორნიკე ხურცია", 64, 0)
sort_users("ბექა ოღრაპიშვილი", 64, 0)
sort_users("ბაჩანა ტყემალაძე", 64, 0)
sort_users("საბა ბეგიაშვილი", 64, 0)
sort_users("დათა თეზელაშვილი", 65, 0)
sort_users("ნიკოლოზ ჩუბუნიძე", 65, 0)
sort_users("გიორგი გლოველი", 65, 0)
sort_users("ზუკა აბაშიძე", 67, 0)
sort_users("დავით ფხაკაძე", 67, 0)
sort_users("გიორგი ხმალაძე", 68, 0)
sort_users("ნიკოლოზ ბაღათურია", 68, 0)
sort_users("biba nikuradze", 69, 0)
sort_users("ირაკლი ოზაშვილი", 70, 0)
sort_users("ლევან სხულუხია", 72, 0)
sort_users("ლუკა მიქუტიშვილი", 72, 0)
sort_users("ირაკლი მებონია", 75, 0)
sort_users("ლუკა მახარაძე", 76, 0)
sort_users("გიორგი თედოზაშვილი", 77, 0)
sort_users("მევლუდი თავაძე", 78, 0)
sort_users("უმარ აბუბაკაროვი", 83, 0)
sort_users("სანდრო სიუკაშვილი", 90, 0)
sort_users("ზურა გვალია", 93, 0)
sort_users("გიორგი ბუბუნაური", 98, 0)
sort_users("ნიკა კახაძე", 106, 0)


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