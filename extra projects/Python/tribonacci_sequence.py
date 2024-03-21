def tribonacci(signature, n):
    if n==0:
        return []
    elif n==1:
        return [signature[0]]
    elif n==2:
        return signature[:2]
    else:
        res_arr=signature
        num1=signature[0]
        num2=signature[1]
        num3=signature[2]
        for i in range(1, n-2):
            num4 = num1 + num2 + num3
            num1 = num2
            num2 = num3
            num3 = num4
            res_arr.append(num4)
        return res_arr
    
signature = input("Enter first, second and third numbers separated by spaces: ")
final_signature = signature.split(" ")
final_signature = [int(x) for x in final_signature]

n = int(input("Enter how many elements you want in sequence: "))
print(F"Your sequence for parameters {[signature]} and {n} is: \n{tribonacci(final_signature, n)}")