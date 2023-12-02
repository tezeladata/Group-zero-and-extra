#Regex count lowercase letters
def lowercase_count(strng):
    count=0
    for i in strng:
        if i!=i.upper():
            count+=1
    return count

#USD => CNY
def usdcny(usd):
    chn=str(usd*6.75)
    if "." in chn:
        if chn[-2]==".":
            chn+="0"
    else:
        chn+="00"
    return "{} Chinese Yuan".format(chn)

#Formatting decimal places #0
def two_decimal_places(n):
    return round(n*100)/100

#Name on billboard
def billboard(name, price=30):
    new=0
    for i in name:
        new+=price
    return new

#How many stairs will Suzuki climb in 20 years?
def stairs_in_20(stairs):
    total=0
    for day in stairs:
        for stair in day:
            total+=stair
    return total*20

#OOP: Object Oriented Piracy
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        return self.draft - self.crew *1.5 > 20
    
#Miles per gallon to kilometers per liter
def converter(mpg):
    return round(mpg * 1.609344 / 4.54609188, 2)