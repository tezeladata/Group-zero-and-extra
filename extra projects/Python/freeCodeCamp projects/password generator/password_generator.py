import random
import string
import pyqrcode

lowercase_letters = [i for i in string.ascii_lowercase]
uppercase_letters = [i for i in string.ascii_uppercase]
digits = [i for i in string.digits]
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[", "]", "{", "}", "|", ";", ":", ",", ".", "/", "<", ">", "?"]

ambiguous_chars = ['l', '1', 'I', '0', 'O']

# For Qrcodes
def create_qr_code(text):
    data = text
    filename = f"./password generator/{data}.png"
    url = pyqrcode.create(data)

    # Creating and saving as image folder
    url.png(filename, scale=15)

def check_strength(password):
    length = len(password)
    has_upper = any(char in uppercase_letters for char in password)
    has_lower = any(char in lowercase_letters for char in password)
    has_digit = any(char in digits for char in password)
    has_special = any(char in special_chars for char in password)

    strength = 0
    if length >= 8:
        strength += 1
    if has_upper:
        strength += 1
    if has_lower:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    return strength

def main():
    while True:
        # Greet
        greeting = "Hello, this is Password Generator"
        print(f'\n{"".join("-" for _ in range(len(greeting)))}')
        print(greeting)
        print(f'{"".join("-" for _ in range(len(greeting)))}\n')
        
        # Display modes
        print(f"You have to choose how many letters you want from these letters:\n\n"
        f"Uppercase: {''.join(uppercase_letters)}|\n"
        f"Lowercase: {''.join(lowercase_letters)}|\n"
        f"Digits: {''.join(digits)}|\n"
        f"Special characters: {''.join(special_chars)}\n")

        # Creating password
        uppers = input("How many uppercase letters do you want in your password? (None if you do not want any) - ")
        lowers = input("How many lowercase letters do you want in your password? (None if you do not want any) - ")
        dig = input("How many digits do you want in your password? (None if you do not want any) - ")
        specials = input("How many special letters do you want in your password? (None if you do not want any) - ")

        # Function for easier creation
        def create_part(num, user_case):
            if num.isdigit():
                if int(num) > 0:
                    return [random.choice(user_case) for _ in range(int(num))]
            return []
            
        # Result
        res_password = create_part(uppers, uppercase_letters) + create_part(lowers, lowercase_letters) + create_part(dig, digits) + create_part(specials, special_chars)

        if not res_password:
            print("Password was not generated because you entered 0 digits")
        else:
            random.shuffle(res_password)
            res_password = "".join(res_password)

            # Excluding ambiguous characters if requested by the user
            include_ambiguous = input("Include ambiguous characters (l, 1, I, 0, O)? Y/N - ")
            if include_ambiguous.lower() != "y":
                res_password = ''.join(char for char in res_password if char not in ambiguous_chars)

            print(f"Your password is: {res_password}")

            is_valid = True
            for i in res_password:
                if i in special_chars:
                    is_valid = False

            if is_valid:
                create_qr_code(res_password)
                print("Your password is also saved as Qrcode")
                # Check password strength
                strength = check_strength(res_password)

                # Displaying strength result
                str_res = f"Password Strength: {strength}/5"
                print(f"\n{'-' * len(str_res)}")
                print(str_res)
                print(f"{'-' * len(str_res)}\n")

        print("Thanks for generating!")

        # Ask user if they want to generate another password
        decision = input("\nGenerate another password? Y/N - ")
        if decision.lower() != "y":
            break

main()