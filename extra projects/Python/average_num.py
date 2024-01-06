print("Hello, this code finds average of written numbers")
n=int(input("How many numbers will you write: "))
num_list=[]
for i in range(0,n):
    num=int(input("Enter number: "))
    num_list.append(num)
avg=sum(num_list)/n
print("average in your numbers is:", avg)
print("Thanks for attention!")