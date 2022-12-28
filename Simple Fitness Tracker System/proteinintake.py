# Description: This program calculates the protein intake of a person
print("\n\t\tYOUR PROTEIN INTAKE\t\t\n")
weight = float(input("Enter your weight in kg: "))
# 1g of protein = 4 calories
# 1g of protein = 0.25 of fat
calories = weight * 2
protein = weight * 2
fat = weight * 0.5
carbohydrates = weight * 2.5
print("\nYour daily protein intake is: " + str(protein) + "g")
print("\nYour fat intake is: " + str(fat) + "g")
print("\nYour carbohydates intake is: " + str(carbohydrates) + "g")
print("\nYour total calories intake is: " + str(calories) + "g\n")
