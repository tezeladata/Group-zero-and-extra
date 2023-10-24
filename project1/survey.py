name = input("What's your name? ")
age = int(input("How old are you? "))
gender = input("What is your gender? male/female: ")
height = float(input("What is your height in m? "))
weight = float(input("What's your weight in kg? "))
bmi = weight / (height**2)
if gender == "male":
    print("\nHis name is", name, "and he is", age, "years old." 
          "\nHe is", height, "meters or", height*100, "cms tall." 
          "\nHe weighs", weight, "kilograms and his body mass index(BMI) is", bmi)
elif gender == "female":
    print("\nHer name is", name, "and she is", age, "years old." 
          "\nShe is", height, "meters or", height*100, "cms tall." 
          "\nShe weighs", weight, "kilograms and her body mass index(BMI) is:", bmi)
else:
    print("Incorrect data")
print("Thanks for attention!")