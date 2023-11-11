def exclamation(word):
  print(word + "!")

exclamation("spam")
exclamation("Nika")

def sum(x, y):
  return x+y

res = sum(42, 7)
print(res)

def family(names, ages):
    print(names, "is", ages, "years old")
family("Data", str(15))
family("Andria", str(8))
family("Nino", str(41))

def my_sum(x, y):
    return x+y #აბრუნებს გამოთვლილ მნიშვნელობას და ინახავს მეხსიერებაში, return-ის შესრულებისას ფუნქცია ასრულებს სიცოცხლეს
my_sum(5,8)
print(my_sum(5,8))

def double(a, b):
  return [a*2, b*2]

x = double(6, 9)
print(x)

def sum(x):
    res = 0
    for i in range(x):
        res+=i
    return res
print(sum(4))


x = 365
y = 7
print(x % y) # find the remainder

"""
docstring
"""
"""hello"""


def print_nums(x):

  for i in range(x):

    print(i)

    return

print_nums(10)

def func(x):

  res = 0

  for i in range(x):

     res += i

  return res

print(func(3))