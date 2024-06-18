def main():
    def encode(n):
        roman_pieces = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = []
        
        for value, symbol in roman_pieces:
            while n >= value:
                result.append(symbol)
                n -= value
        
        return "".join(result)
    
    def decode(n):
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        for char in reversed(n):  # Reverse the string to simplify comparison
            current_value = roman_values[char]
            
            if current_value >= prev_value:
                total += current_value
            else:
                total -= current_value
            
            prev_value = current_value
        
        return total
    
    print("Hello, this is Roman numerals encoder/decoder")
    
    while True:
        choice = input("Encode or decode? ").lower()
        
        if choice == "encode":
            try:
                number = int(input("Enter natural number: "))
                if number <= 0:
                    raise ValueError("Input must be a positive integer.")
                
                print(f"Your number in Roman form is: {encode(number)}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "decode":
            try:
                roman_number = input("Enter your Roman number: ").upper()
                result = decode(roman_number)
                print(f"Your Roman number in natural form is: {result}")
            except ValueError as e:
                print(f"Error: {e}")
        
        else:
            print("Invalid input!")
        
        again = input("Again? Y/N - ").lower()
        if again != "y":
            break
    
    print("Thanks for your attention!")

main()