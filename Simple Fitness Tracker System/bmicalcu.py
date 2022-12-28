
print("\n\t\tBMI CALCULATOR\t\t\n")
weight = float(input("Enter your weight in pounds(lbs): "))
height = float(input("Enter your height in inches(in): "))
bmi = (weight/height**2)*703
print(round(bmi, 2))
if bmi < 18.5:
    print("Underweight Range")
elif bmi >= 18.5 or bmi <= 24.9:
    print("You're in the Healthy Weight Range!")
elif bmi >= 25 or bmi <= 29.9:
    print("Overweight Range")
elif bmi >= 30:
    print("Obese Range")