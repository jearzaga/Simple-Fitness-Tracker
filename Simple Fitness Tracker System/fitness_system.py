print("\nWhat do you want to use?\n• Choose 1 for BMI Calculator\n• Choose 2 to track your Macronutrient\n• Choose 3 to know your Calorie Intake\n")
choices = int(input("Your choice: "))
if choices == 1:
    from bmicalcu import *  #imports the functionality of bmicalculator.py
elif choices == 2:
    from proteinintake import * #imports the functionality of proteinintake.py
elif choices == 3:
    def title():
        print("\n\t\tCALORIE INTAKE\t\t\n")
    # user's information to calculate their calorie maintenance
    # Mifflin-St Jeor formula
    title()
    sex = input("Sex [M or F]: ")
    age = int(input("Age: "))
    height = float(input("Height (cm): "))
    weight = float(input("Weight (kg): "))
    print("\nPhysical Activity Level [PAL]\n• Press 1 for little or no exercise,\n• Press 2 for light exerise 1-2 times/week,\n• Press 3 for moderate exercise 2-3 times/week,\n• Press 4 for hard exercise 3-5 times/week.\n• Press 5 if you got a physical job or perform hard exercise 6-7 times/week,\n• Press 6 for Professional Athletes. ")
    act = int(input("PAL: "))
    #computation for M
    if sex == 'M':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
        if act == 1:
            pal = bmr * 1.2
            print(round(pal, 2))
        elif act == 2:
            pal = bmr * 1.4
            print(round(pal, 2))
        elif act == 3:
            pal = bmr * 1.6
            print("Your calorie maintenance is: " + str(round(pal, 2)))
        elif act == 4:
            pal = bmr * 1.75
            print(round(pal, 2))
        elif act == 5:
            pal = bmr * 2.0
            print(round(pal, 2))
        elif act == 6:
            pal = bmr * 2.4
            print(round(pal, 2))
        else:
            print("Invalid Number!")
    #computation for F
    elif sex == 'F':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
        if act == 1:
            pal = bmr * 1.2
            print(round(pal, 2))
        elif act == 2:
            pal = bmr * 1.4
            print(round(pal, 2))
        elif act == 3:
            pal = bmr * 1.6
            print("Your calorie maintenance is: " + str(round(pal, 2)))
        elif act == 4:
            pal = bmr * 1.75
            print(round(pal, 2))
        elif act == 5:
            pal = bmr * 2.0
            print(round(pal, 2))
        elif act == 6:
            pal = bmr * 2.4
            print(round(pal, 2))
        else:
            print("Invalid Number!")
    else: 
        print("Invalid Choices!\n\n")
    #calorie deficit and surplus
    print("\nDo you want to calculate your calorie deficit or surplus?\n• Press 1 for calorie deficit,\n• Press 2 for calorie surplus.")
    choices = int(input("Your choice: "))
    if choices == 1:
        print("\nHow many calories do you want to lose?")
        lose = int(input("Calories: "))
        print("\nYour calorie deficit is: " + str(round(pal - lose, 2)))
        print("\n\n")
    elif choices == 2:
        print("\nHow many calories do you want to gain?")
        gain = int(input("Calories: "))
        print("\nYour calorie surplus is: " + str(round(pal + gain, 2)))
        print("\n\n")
    else: 
        print("Invalid Choices!\n\n") #if the user enters a wrong input
else: 
    print("Invalid Choices!") #if the user enters a wrong input
