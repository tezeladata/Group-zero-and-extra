import random
import time

all_leaders = ["Erekle Kilasonia", "Giorgi Khmaladze", "Ana Puturidze", "Giorgi Vanishvili", "Sophia Gorgadze", "Giorgi Tskhadadze",  "Giorgi Ziraqashvili", "Giorgi Giorgobiani", "Andria Korchilava", "Aleksandre Chankvetadze", "Nikoloz Tchitadze", "Guram Papunashvili", "Levani Samsonidze", "Zuka Qoridze", "Nikoloz Tevdoradze", "Nikoloz Edisherashvili", "Lika Chkhikvadze", "Luka Dgebuadze", "Goga Chalauri", "Giorgi Bibilashvili", "Daniel Abramiani", "Aleksandre Dzukaevi", "Davit Adeishvili"]

winners = []
def lucky_leader(all, res_arr):
    print("Lucky leader is:\n")

    # Simple timer
    start = 10
    while start > 0:
        print(start)
        start -= 1
        time.sleep(1)

    # Choose and store
    lucky = random.choice(all)
    all.remove(lucky)
    res_arr.append(lucky)

    # Print
    print(f'\n{"-"*(len(lucky)*2)}')
    print(f"{lucky.upper()}!!!")
    print(f'{"-"*(len(lucky)*2)}\n\n')

    return

lucky_leader(all_leaders, winners)
lucky_leader(all_leaders, winners)
lucky_leader(all_leaders, winners)

# Final
print(f"All winners are:\n\n{winners[0].upper()}\n{winners[1].upper()}\n{winners[2].upper()}")