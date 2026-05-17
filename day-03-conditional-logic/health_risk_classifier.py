print("Health Risk Classifier")

bmi = float(input("Enter BMI: "))

if bmi >= 40:
    category = "Severe Obesity"
    risk = "Very High Risk"
elif bmi >= 30:
    category = "Obesity"
    risk = "High Risk"
elif bmi >= 25:
    category = "Overweight"
    risk = "Moderate Risk"
elif bmi >= 18.5:
    category = "Normal Weight"
    risk = "Low Risk"
else:
    category = "Underweight"
    risk = "Potential Nutritional Risk"

print()
print(f"BMI Category: {category}")
print(f"Health Classification: {risk}")
