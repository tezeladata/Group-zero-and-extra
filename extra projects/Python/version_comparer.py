def compare_versions(version1,version2):
    def calc(v):
        start = 1
        res = 0
        
        for i in [int(i) for i in v.split(".")]:
            res += i*start
            start /= 10
        
        return res

    v1, v2 = calc(version1), calc(version2)
        
    return f"{version1} >= {version2}" if v1>=v2 else f"{version2} > {version1}"

print(compare_versions(version1=input("Enter version1 value, e.g 10.1.2 - "), version2=input("Enter version2 value, e.g 5.3.0 - ")))