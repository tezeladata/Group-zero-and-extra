print("Hello, this is currency exchange.")
currency = input("Choose your currency: gel/usd/euro/gbp ")
money = int(input("How much money are you exchanging? "))

while currency == "gel":
    sec_currency = input("In which currency will you exchange: usd/euro/gbp ")
    if sec_currency == "usd":
        print("After exchanging you have", money*0.37, "dollars.")
        break
    elif sec_currency == "euro":
        print("After exchanging you have", money*0.35, "euros.")
        break
    elif sec_currency == "gbp":
        print("After exchanging you have", money*0.31, "pounds.")
        break
    else:
        print("Incorrect currency.")
        break

while currency == "usd":
    sec_currency = input("In which currency will you exchange: gel/euro/gbp ")
    if sec_currency == "gel":
        print("After exchanging you have", money*2.69, "gels.")
        break
    elif sec_currency == "euro":
        print("After exchanging you have", money*0.95, "euros.")
        break
    elif sec_currency == "gbp":
        print("After exchanging you have", money*0.82, "pounds.")
        break
    else:
        print("Incorrect currency.")
        break

while currency == "euro":
    sec_currency = input("In which currency will you exchange: gel/usd/gbp ")
    if sec_currency == "gel":
        print("After exchanging you have", money*2.84, "gels.")
        break
    elif sec_currency == "usd":
        print("After exchanging you have", money*1.05, "dollars.")
        break
    elif sec_currency == "gbp":
        print("After exchanging you have", money*0.87, "pounds.")
        break
    else:
        print("Incorrect currency.")
        break

while currency == "gbp":
    sec_currency = input("In which currency will you exchange: gel/usd/euro ")
    if sec_currency == "gel":
        print("After exchanging you have", money*3.27, "gels.")
        break
    elif sec_currency == "usd":
        print("After exchanging you have", money*1.22, "dollars.")
        break
    elif sec_currency == "euro":
        print("After exchanging you have", money*1.15, "euros.")
        break
    else:
        print("Incorrect currency.")
        break
print("This currency exchange works with 10/18/2023 data.")
print("Thanks for attention!")