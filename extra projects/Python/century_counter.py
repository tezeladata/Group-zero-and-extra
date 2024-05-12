def what_century(year):
    century = str((int(year) + 99) // 100)

    if century.endswith("1") and century != "11":
        return century + "st"
    
    if century.endswith("2") and century != "12":
        return century + "nd"
    
    if century.endswith("3") and century != "13":
        return century + "rd"
    
    return century + "th"