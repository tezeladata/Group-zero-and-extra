# 1
def task1(user_str):
    n = 0
    comparison_count = 0
    increment_count = 0

    for i in user_str:
        n += 1
        comparison_count += 1
        if i.isupper():
            increment_count += 1
    
    return comparison_count, increment_count


compare, increment = task1("abcdEFGH")
print(f"Comparison count: {compare}, increment count: {increment}")

# After the result, we can see, that comparison count is same as the length of our string. But increment is dependent on the upper case letters.
# Increment variable will have same value as the count of uppercase letters.
# Increment variable value will have minimal value - 0, when there are only lowercase letters in text
# Iincrement variable's maximum value will be n - length of string, when all of the letters are uppercase.



# 2
def task2(numbers):
    sum_of_nums = 0
    count = 0

    for i in numbers:
        sum_of_nums += i
        count += 1

    avg = sum_of_nums / count
    return avg

average = task2({1, 2, 3, 4, 5, 6, 7})
print(f"Average of your numbers is: {average}")

# In task 2, we had following operations: declare, reassign, increment, divide
# there were 3 declarations, reassigning was done 2n times (n = length of set), incrementation was done n times, division was done 1 time

def task2_extra(numbers):
    n = 0
    product = 1

    for num in numbers:
        n += 1
        product *= num
    
    result = product ** (1 / n)
    return result

average2 = task2_extra({1, 2, 3, 4, 5, 6, 7})
print(f"Average geometrical of your numbers is: {average2}")



# 3
def task3(numbers):
    num1 = numbers[0]
    num2 = numbers[1]
    num3 = numbers[2]

    if type(num1) == int:
        if type(num2) == int:
            if type(num3) == int:

                # After checking input datatypes
                if num1 != num2:
                    if num1 != num3:
                        if num2 != num3:
                            return True
    return False

same_or_not = task3([1, 2, 3])
print(f"Result is: {same_or_not}")

# one comparation is minimal, because first variable will always be checked about it's datatype
# If all elements in numbers array have datatype of int, four comparations is minimal.
# what parts will arrays have in one whole, which have all distinct numbers and arrays which don't have distinct numbers



# კონიუქცია - and
# დიზიუნქცია - or


# ფუნქცია f არის შესაბამისობა ორ A და B სიმრავლეს (A განსაზღვრის არესა და B მნიშვნელობათა სიმრავლეს) შორის, როდესაც: 1. განსაზღვრის არის ერთ ელემენტს შეესაბამება მნიშვნელობათა სიმრავლის მხოლოდ ერთი ელემენტი
# 2. განსაზღვრის არის ყოველ ელემენტს აქვს შესაბამისი ელემენტი მნიშვნელობათა სიმრავლეში.