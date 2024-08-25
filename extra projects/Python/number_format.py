def number_format(n):
    new = list(str(n))
    if new[0] == "-": new = [f"-{new[1]}"] + new[2:]
    else: new = list(str(n))
    
    parts = []
    while len(new) > 0:
        parts.append(''.join(new[-3:]))
        new = new[:-3]
    
    return ",".join(reversed(parts))

print(number_format(n=int(input("Enter integer: "))))