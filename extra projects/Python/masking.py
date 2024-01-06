def masking(str):
    if len(str)<=4:
        return str
    else:
        new=""
        a=len(str)
        for i in range(a-4):
            new+="#"
        new+=str[-4:]
    return new
print(masking(str=input("Enter content which will then be maskified: ")))