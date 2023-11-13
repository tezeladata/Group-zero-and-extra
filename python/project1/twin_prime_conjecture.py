print("Hello, this code writes you twin prime in selected range!")
def prime_num(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def generating_twins(lower_limit, upper_limit):
    for i in range(lower_limit, upper_limit):
        j=i+2
        if prime_num(i) and prime_num(j):
            print("Twin primes are: {} and {} for selected range.".format(i, j))
generating_twins(2, upper_limit=int(input("Select upper limit: ")))