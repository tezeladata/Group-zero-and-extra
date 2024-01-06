print("Hello, this is currency exchange.")
currency = input("Choose your currency: gel/usd/euro/gbp ")
money = int(input("How much money are you exchanging? "))
if currency == "gel":
    sec_currency = input("In which currency will you exchange: usd/euro/gbp ")
    if sec_currency == "usd":
        print("After exchanging you have", money*0.37, "dollars.")
    elif sec_currency == "euro":
        print("After exchanging you have", money*0.35, "euros.")
    elif sec_currency == "gbp":
        print("After exchanging you have", money*0.31, "pounds.")
    else:
        print("Incorrect currency.")

if currency == "usd":
    sec_currency = input("In which currency will you exchange: gel/euro/gbp ")
    if sec_currency == "gel":
        print("After exchanging you have", money*2.69, "gels.")
    elif sec_currency == "euro":
        print("After exchanging you have", money*0.95, "euros.")
    elif sec_currency == "gbp":
        print("After exchanging you have", money*0.82, "pounds.")
    else:
        print("Incorrect currency")
if currency == "euro":
    sec_currency = input("In which currency will you exchange: gel/usd/gbp ")
    if sec_currency == "gel":
        print("After exchanging you have", money*2.84, "gels.")
    elif sec_currency == "usd":
        print("After exchanging you have", money*1.05, "dollars.")
    elif sec_currency == "gbp":
        print("After exchanging you have", money*0.87, "pounds.")
    else:
        print("Incorrect currency.")

if currency == "gbp":
    sec_currency = input("In which currency will you exchange: gel/usd/euro ")
    if sec_currency == "gel":
        print("After exchanging you have", money*3.27, "gels.")
    elif sec_currency == "usd":
        print("After exchanging you have", money*1.22, "dollars.")
    elif sec_currency == "euro":
        print("After exchanging you have", money*1.15, "euros.")
    else:
        print("Incorrect currency.")
print("This currency exchange works with 10/18/2023 data.")
print("Thanks for attention!")