def rms():
    def intro():
        print("Hello, this is recipe management system!")
        print("Here you can store and update your recipes!\n\n")

    # Intro part:
    intro()

    # Function to sign up user
    def sign_up():
        print("First of all, you have to sign up:")

        def is_valid_text(value):
            return value.isalpha()

        def is_valid_password(value):
            return value.isalnum()

        # What user will be asked
        prompts = {
            "name": "Enter your name: ",
            "surname": "Enter your surname: ",
            "password": "Enter password (Only alphanumeric letters) - "
        }

        # Validations using functions created above
        validations = {
            "name": is_valid_text,
            "surname": is_valid_text,
            "password": is_valid_password
        }

        credentials = {}

        for field, prompt in prompts.items():
            value = input(prompt)

            # When function returns False:
            while not validations[field](value):
                # Asking for input again
                value = input(prompt)
            # If input is valid, it will be added to credentials dict
            credentials[field] = value

        print("\nYou have succesfully signed in!\n")

        # Returning user credentials
        return credentials
    
    # To store user info
    user_credentials = sign_up()

    # Function to log in 
    def log_in():
        print("Now you have to log in!")
        for field, prompt in user_credentials.items():
            ans = input(f"Enter {field}: ")
            while ans != user_credentials[field]:
                print("Incorrect!")
                ans = input(f"Enter {field}: ")
        
        print("You have succesfully logged into the system!")

        # Displaying user info
        res = f"Your data: {[user_credentials[i] for i in user_credentials]}"

        print(f"\n{''.join(['-' for _ in range(len(res))])}")
        print(res)
        print(f"{''.join(['-' for _ in range(len(res))])}\n")

    # for user to log in
    log_in()

    # Recipe dict
    recipe_dict = dict()

    # Main logic
    def main(recipe_dict):
        # adding items
        def add_items(recipe_dict):
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients of your meal: ")
            instructions = input("Enter cooking instructions: ")

            try:
                cooking_time = float(input("Enter cooking time in minutes: "))
            except ValueError:
                print("You did not enter a number")

            recipe_dict[name] = [ingredients, instructions, cooking_time]
            print("You have succesfully added a recipe")

            return recipe_dict

        # editing items
        def edit_items(recipe_dict):
            name = input("Enter a recipe name which will have changed description: ")

            while name not in recipe_dict.keys():
                print("Incorrect name")
                name = input("Enter a recipe name again: ")
            
            # dict value:
            dict_val = recipe_dict[name]
            
            decision = input("Which detail would you like to change? (ingredients / instructions / cooking time)")
            if decision not in ["ingredients", "instructions", "cooking time"]:
                print("Incorrect detail")
            else:
                if decision == "ingredients":
                    dict_val[0] = input("Enter changed ingredients: ")
                elif decision == "instructions":
                    dict_val[1] = input("Enter changed instructions: ")
                else:
                    dict_val[2] = input("Enter changed cooking time: ")
            
            print("You have succesfully edited your recipe")

            return recipe_dict

        # removing items
        def remove_items(recipe_dict):
            name = input("Enter a recipe name you want to remove: ")

            while name not in recipe_dict.keys():
                print("Incorrect name")
                name = input("Enter a recipe name again: ")

            recipe_dict.pop(name)

            print("You have succesfully deleted your recipe")

            return recipe_dict
                
        # Logic
        print(f"Right now, your recipes look like this: \n{recipe_dict}")
        print("You can add / edit / delete your recipes")

        decision = input("Which operation? - ")
        if decision.lower() == "add":
            recipe_dict = add_items(recipe_dict)
            print(f"\nRight now, your recipes look like this: \n{recipe_dict}\n")
        elif decision.lower() == "edit":
            recipe_dict = edit_items(recipe_dict)
            print(f"\nRight now, your recipes look like this: \n{recipe_dict}\n")
        elif decision.lower() == "delete" or decision.lower() == "del":
            recipe_dict = remove_items(recipe_dict)
            print(f"\nRight now, your recipes look like this: \n{recipe_dict}\n")

        again = input("Continue? Y / N: ")

        if again.lower() == "y" or again.lower() == "yes":
            main(recipe_dict)  # Call main function recursively with updated recipe_dict
        else:
            print("Thanks for your attention")
            return

    main(recipe_dict)

rms()