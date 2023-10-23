import random
print("Hello, this is a random password generator")
Characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"

lenght = int(input("What length would you like your password to be : "))
count = int(input("How many passwords would you like : "))
for x in range(0, count):
    password = ""
    for x in range(0, lenght):
        password_char = random.choice(Characters)
        password = password + password_char
    print("Here is your random password : " , password)