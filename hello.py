print("Welcome to the personalised user profile generator!")
#The purpose of the welcome message is to greet clients when opening the program

name = input("Please enter your full name")

age = input("Please enter your age")

height = input("Please enter your height")

favourite_programming_language = input("Please list your favourite progamming language")

favouritre_number = input("Please enter your favourite number")

short_description_of_yourself = input("Please enter a short description of yourslef")
#This is collecting and processing user input

age = float(age)

height = int(height)

favourite_number = str(favouritre_number)
#converting 

first_name= name.split()[0]
print(f"Hello, {first_name}! ")
#slicing