print("Medication Dose Calculator")

def calculate_dose(weight_kg, dose_mg_per_kg):
    return weight_kg * dose_mg_per_kg


weight = float(input("Enter patient weight in kg: "))
dose_per_kg = float(input("Enter prescribed dose (mg/kg): "))

total_dose = calculate_dose(weight, dose_per_kg)

print()
print(f"Total dose: {total_dose:.2f} mg")
