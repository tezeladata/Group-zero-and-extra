#  Event detected during execution that interrupts the flow of a programme

# try: 
#     numb = int(input("Enter number: "))
#     divisor = int(input("Enter divisor: "))
#     res = numb / divisor
#     print(res)
# except ZeroDivisionError:
#     print("You cannot divide by zero")
# except ValueError:
#     print("You can only divide by number")
# except Exception:
#     print("Something went wrong")


# We can also show errors:
# try: 
#     numb = int(input("Enter number: "))
#     divisor = int(input("Enter divisor: "))
#     res = numb / divisor
#     # Printing result if no exceptions, in else code block
# except ZeroDivisionError as e: # as e means that as exception
#     print(e)
#     print("You cannot divide by zero")
# except ValueError as e:
#     print(e)
#     print("You can only divide by number")
# except Exception as e:
#     print(e)
#     print("Something went wrong")
# else:
#     print(res)
# # finally is always at the end, whether or not we catch an exception, it will always execute
# finally:
#     print("You made it")

# Task:
def get_credentials():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    print("Account created!")
    result = {
        "Name": name,
        "Surname": surname
    }
    return result

def check_credentials():
    new_result = get_credentials()
    credentials_arr = []
    for key, value in new_result.items():
        credentials_arr.append(value)

    print("\nChecking your data:\n")

    try:
        check_name = input("Enter name of your account: ")
        check_surname = input("Enter surname of your account: ")

        counter = 0
        while check_name != credentials_arr[0] or check_surname != credentials_arr[1]:
            counter += 1
            if counter >= 3:
                raise ValueError("Too many failed login attempts. Account locked.")
            print("Invalid credentials. Please try again.")
            check_name = input("Enter name of your account: ")
            check_surname = input("Enter surname of your account: ")
    except ValueError as e:
        print(e)
    except Exception:
        print("Invalid")
    else:
        print("Login successful!")

check_credentials()