# arguments preceded by an identified when we pass them to a function
# The order of the arguments doesn't matter, unlike positional arguments
# Python knows the names of the arguments that our function receives

# Positional arguments:
def full_name(f_name, m_name, l_name):
    return f"Hello {f_name} {m_name} {l_name}"
print(full_name("David", "", "Tezelashvili"))

# Improved version:
def full_name(f_name, m_name, l_name):
    return f"{f_name} {m_name} {l_name}"
print(full_name(l_name="Tezelashvili", m_name="", f_name="David"))

# This time we use identifiers such as l_name, m_name and f_name and positions of arguments does not matter

# Task:
def calculate_shopping_cart_cost(item1, item2, item3, item4):
    # Creating a list with four parameters:
    items_list = [item1, item2, item3, item4]
    prices = {}
    for list in items_list:
        item = list[0]
        item_total_price = list[1] * list[2]
        prices[f"{item}"] = item_total_price
    return f"Dictionary for items and their total prices is:\n{prices}"

print(calculate_shopping_cart_cost(item4=["Banana", 0.30, 10], item2=["Apple", 0.25, 5], item3=["Cheese", 20, 2], item1=["Bread", 1, 3]))