def conversion():
    print("Hello, this code turns integers to binary!")
    number=int(input("Enter number: "))
    binary=[]
    while number>0:
        dig=number%2
        binary.append(dig)
        number=number//2
    binary=binary[::-1]
    binary=[str(current_integer) for current_integer in binary]
    string_value = "".join(binary)
    result = int(string_value)
    print("Binary value is {}.".format(result))
    print("Thanks for attention!")
conversion()