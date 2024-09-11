def change_case(identifier, targetCase):
    if identifier == "": return ""

    if '-' in identifier and identifier.islower(): parts = identifier.split('-')
    elif '_' in identifier and identifier.islower(): parts = identifier.split('_')
    elif " " in identifier and identifier.islower(): parts = identifier.split(" ")

    # Camel
    elif '-' not in identifier and '_' not in identifier:
        parts = []
        start = 0
        for i in range(1, len(identifier)):
            if identifier[i].isupper():
                parts.append(identifier[start:i])
                start = i
        parts.append(identifier[start:])
    else:
        return None

    if any(not part.isalpha() for part in parts): return None

    if targetCase == "snake":
        return "_".join(parts).lower()
    elif targetCase == "kebab":
        return "-".join(parts).lower()
    elif targetCase == "camel":
        return parts[0] + "".join(part.title() for part in parts[1:])

print(change_case(identifier=input("Enter your text: "), targetCase=input("Choose case: snake/camel/kebab: ").lower()))