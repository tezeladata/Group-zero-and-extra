def simplify(number):
    if number == 0:
        return ""

    res = []
    for i in range(len(str(number))):
        res.append(f"{str(number)[i]}*{'1' + '0' * (len(str(number)) - i - 1)}")
    res[-1] = res[-1].split("*")[0]
    res = [i for i in res if i.split("*")[0] != '0']

    return "+".join(res)