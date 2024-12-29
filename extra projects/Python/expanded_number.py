def expanded_form(num):
    # left part
    left, left_res = str(num).split(".")[:1][0], []
    ln = len(left)

    for i in range(len(left)):
        if left[i] != "0": left_res.append(left[i] + "0" * len(left[i + 1:]))

    # right part
    right, right_res = str(num).split(".")[1:][0], []
    ln, count_zero = len(right), 1

    for i in right:
        if i != "0": right_res.append(f"{i}/{'1' + '0' * count_zero}")
        count_zero += 1

    # final
    res = left_res + right_res
    return " + ".join(res)