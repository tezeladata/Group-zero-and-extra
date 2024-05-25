def rpm(num1, num2):
    # halver
    def halver(num):
        arr = []

        while num != 1:
            arr.append(num)
            num //= 2
        arr.append(1)

        return arr

    def doubler(num):
        arr = [num]

        for _ in range(len(halver(num1)) -1):
            arr.append(num*2)
            num *= 2

        return arr

    rows = [[halver(num1)[i], doubler(num2)[i]] for i in range(len(halver(num1)))]

    updated = [rows[i] for i in range(len(rows)) if rows[i][0] %2 != 0]

    final = sum([updated[i][1] for i in range(len(updated))])

    return final

print(rpm(int(input("Enter number1: ")), int(input("Enter number2: "))))