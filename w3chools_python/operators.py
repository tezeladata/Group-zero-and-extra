#Python divides the operators in the following groups:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators
                                    #assignment operators x=12
print(12+5) #addition - +           x+=5
print(12-8) #subtraction - -        x-=8
print(12*7) #multiplication - *     x*=7
print(12/4) #division - /           x/=4
print(12%3) #modulus - %            x%=3
print(12**3) #Exponentiation - **   x**=3
print(12//6) #floor division - //   x//=6
#Floor division is a division operation that rounds the result down to the nearest whole number or integer, which is less than or equal to the normal division result.

#comparison operators
print(3==3)          #equal
print(5!=7)          #not equal
print(9>23)          #is greater than
print(4<6)           #is less than
print(7>=4)          #greater than or equal to	
print(4<=2)          #is less than

#logical operators
print(4>5 and 7==7)  #returns True if both statements are true	
print(4<6 or 5>8)    #returns True if one of the statements is true	
print(not(5>3 and 2<10))   #Reverse the result, returns False if the result is true	

#identify operators
a=[2, 5]
b=[3, 12]
c=a
print(a is c)        #returns True if both variables are the same object	
print(a is not b)    #Returns True if both variables are not the same object	

#membership operators
a=[3,2,34,22,87]
print(87 in a)       #returns True if a sequence with the specified value is present in the object
print(2 not in a)	 #returns True if a sequence with the specified value is not present in the object	