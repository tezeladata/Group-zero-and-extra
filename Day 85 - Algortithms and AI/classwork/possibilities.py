import random

choices = [random.randint(0, 10000) for _ in range(4)]

one, two, three, four = 0, 0, 0, 0

for _ in range(1000):
    i = random.choice(choices)

    if i == choices[0]:
        one += 1
    elif i == choices[1]:
        two += 1
    elif i == choices[2]:
        three += 1
    else:
        four += 1

parts = "% ".join([str(one / 10), str(two / 10), str(three / 10), str(four / 10)]) + "%"
print(parts)