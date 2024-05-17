import random

def mastermind():
    correct_num = str(random.randint(1000, 9999))

    base = ["X" for _ in range(4)]
    print(f"Your number now looks like: {'-'.join(base)}")

    tries = 0

    while "".join(base) != correct_num:
        count = 0  # Reset count for each guess
        user_num = input("Enter a 4 digit number to guess: ")

        if len(user_num) != 4 or not user_num.isdigit():
            print("Please enter a 4 digit number.")
            continue

        for i in range(4):
            if user_num[i] == correct_num[i]:
                count += 1
                base[i] = correct_num[i]

        if count == 0:
            print(f"\nNot quite right, you got none of the digits correctly")
        elif count == 1:
            print(f"\nNot quite right, you got {count} digit correctly")
        else:
            print(f"\nNot quite right, you got {count} digits correctly")

        print(f"After your guess, Your number now looks like: {'-'.join(base)}\n")

        tries += 1

    tries += 1
    res = f"You guessed the number - {correct_num} in {tries} tries."
    decoration = "".join("-" for _ in range(len(res)))

    print(f"\n{decoration}")
    print("Conrgats, you became Mastermind")
    print(res)
    print(f"{decoration}\n")


def to_list(num):
    return [str(i) for i in str(num)]

mastermind()