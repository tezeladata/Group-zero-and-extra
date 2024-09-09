def mirror(text):
    text = text.split(" ")
    ln = len(sorted(text, key=len)[-1])

    res = ["*" * (ln + 4) + "\n"]
    for i in text: res.append(f"* {i}{' ' * (ln - len(i))} *\n")
    res.append("*" * (ln + 4))
    return "".join(res)


print(mirror(text=input("Enter text: ")))