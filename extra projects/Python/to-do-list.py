def to_do_list():
    # Main functions
    def add_or_edit_items(user_dict):
        name = input("Enter name of your task: ")
        data = input("Enter description of your task: ")
        user_dict[name] = data

    def delete_items(user_dict):
        name = input("Enter name of the task you want to delete: ")
        del user_dict[name]

    print("Hello, this is a simple To-do list")
    user_dict = dict()

    # Main logic
    def main_logic(user_dict):
        print(f"Your list now looks like this: {user_dict}")
        print("You can add / edit / remove items from your list")
        choice = input("Select operation: ")

        if choice.lower() == "add":
            add_or_edit_items(user_dict)
            print("")
            print(user_dict)
            print("")
        elif choice.lower() == "edit":
            add_or_edit_items(user_dict)
            print("")
            print(user_dict)
            print("")
        elif choice.lower() == "remove":
            delete_items(user_dict)
            print("")
            print(user_dict)
            print("")
        else:
            print("Incorrect operation!")
            print("")
            print(user_dict)
            print("")

    main_logic(user_dict)

    user_decision = input("Continue? Y/N - ")

    while user_decision.lower() == "y":
        main_logic(user_dict)
        user_decision = input("Continue? Y/N - ")
    print("Thanks for the attention!")

to_do_list()