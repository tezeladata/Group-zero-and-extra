#using functions
#def - ფუქნცია

#პარამეტრი - name
#არგუმენტი - კონკრეტული სახელი მაგ. nika
def misalmeba(name, age):
    print("mogesalmebi " + name)
    print("sheni asakia ", age) # , გამოიყენება int-თან

misalmeba("nika", 13)
misalmeba("luka", 14)
misalmeba("gabriel", 15)
misalmeba("sandro", 16)

numbers = list(range(10))
print(numbers)

numbers = list(range(3, 8))
print(numbers)

def greet(welcome):
    return "hello world!"

numbers = list(range(5, 20, 2))
print(numbers)

x = list(range(7, 3, -1))
print(x)

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[7:])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2]) #ორი ნაბიჯით გამოტოვება
print(squares[2:8:3]) #2-იდან 8-მდე ყოველი მესამე დაიპრინტოს

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4]) #1-იდან დაიწყებს, ბოლომდე წავა და 4-ს გამოტოვებს

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1]) #1-დან 64-ის ჩათვლით - მეორე ელემენტიდან ბოლოს წინის ჩათვლით
#-1 არის ნეგატიური ინდექსი

nums = [5, 42, 7, 1, 0]
res = nums[::-1] #::-1 არის სიის შეტრიალება
print(res)