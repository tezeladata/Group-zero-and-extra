# Write out numbers - 5kyu
def number2words(n):
    def one_digit(n):
        switcher = {
            0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
            5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"
        }
        return switcher.get(n, "")

    def two_digits(n):
        if 10 <= n < 20:
            switcher = {
                10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
                14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
                18: "eighteen", 19: "nineteen"
            }
            return switcher.get(n, "")
        else:
            switcher = {
                20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
                60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
            }
            return switcher.get(n - n % 10, "") + ("" if n % 10 == 0 else "-" + one_digit(n % 10))

    def three_digits(n):
        if n == 0: return ""
        elif n < 100: return two_digits(n)
        else: return one_digit(n // 100) + " hundred" + ("" if n % 100 == 0 else " " + two_digits(n % 100))

    def number_to_words(n):
        if n == 0: return "zero"
        elif n < 1000: return three_digits(n)
        elif n < 1000000: return three_digits(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + three_digits(n % 1000))

    res = number_to_words(n).split(" ")
    res = [i[1:] if i[0] == "-" else i for i in res]
    return " ".join(res)

print(number2words(n=int(input("Enter number: "))))