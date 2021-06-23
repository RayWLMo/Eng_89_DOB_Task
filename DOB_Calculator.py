user_prompt = True
name = input("What is your name?    ")

while user_prompt:  # While loop to ask for user's age
    age = input("How old are you?    ")
    if age.isdigit() == True and int(age) < 150:
        while user_prompt:  # Second while loop to ask for user's month of birth
            month = int(input("What month were you born in (as a digit)?    "))
            if month <= 6 and month > 0:
                year_of_birth = 2021 - int(age)
                print(f"OMG {name.capitalize()}, you are {age} years old so you were born in {year_of_birth}")
                user_prompt = False
            elif month > 6 and month <= 12:
                year_of_birth = 2021 - int(age) - 1
                print(f"OMG {name.capitalize()}, you are {age} years old so you were born in {year_of_birth}")
                user_prompt = False
            elif age == "exit":
                print("Thank you for using this program")
                break
            else:
                print("Month is invalid, make sure the month is in digits, i.e October is 10 "
                      "or enter 'exit' to close the program")
    elif int(age) >= 150:
        print(f"Your age isn't {age}, please enter a valid age in digits or enter 'exit' to close the program")
    elif age == "exit":
        print("Thank you for using this program")
        break
    else:
        print("The age you have entered is invalid, please enter the "
              "age in digits or enter 'exit' to close the program")
