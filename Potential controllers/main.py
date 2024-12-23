import random
import time

# took out these controllers from list: "khuberishvili", "grdzelishvili", "motiashvili", "gvritishvili", "tsitlauri"
# december first winners - abashidze, alavidze, kvaratskhelia
all_leaders = [
"kilasonia", "khuskivadze", "vanishvili", "gurgenidze", "abramiani", "svanidze", "vakhtangashvili", "papunashvili", "razmadze", "kobakhidze", "arakhamia", "kochalidze", "tchitadze"
]

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