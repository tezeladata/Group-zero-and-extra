print("This calculator shows inflation of USD by decades.")
print("If I purchased item in 1920/1930/1940 \n"
      "1950/1960/1970/1980/1990/2000/2010/2020? \n")
decade=int(input("your decade: "))
price=int(input("Your item is worth: "))
if decade==1920:
    print("This item would cost", price*15.389, "USD in 2023")
elif decade==1930:
    print("This item would cost", price*18.43, "USD in 2023")
elif decade==1940:
    print("This item would cost", price*21.985, "USD in 2023")   
elif decade==1950:
    print("This item would cost", price*12.771, "USD in 2023")   
elif decade==1960:
    print("This item would cost", price*10.398, "USD in 2023")   
elif decade==1970:
    print("This item would cost", price*7.933, "USD in 2023")   
elif decade==1980:
    print("This item would cost", price*3.735, "USD in 2023")   
elif decade==1990:
    print("This item would cost", price*2.355, "USD in 2023")   
elif decade==2000:
    print("This item would cost", price*1.787, "USD in 2023") 
elif decade==2010:
    print("This item would cost", price*1.412, "USD in 2023") 
elif decade==2020:
    print("This item would cost", price*1.189, "USD in 2023") 