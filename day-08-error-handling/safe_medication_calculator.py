print("Safe Medication Calculator")


def convert_lbs_to_kg(weight_lbs):
    return weight_lbs * 0.453592


def calculate_dose(weight_kg, dose_mg_per_kg):
    return weight_kg * dose_mg_per_kg


try:
    unit = input("Is the patient weight in kg or lb? ").lower().strip()

    if unit not in ["kg", "lb"]:
        raise ValueError("Weight unit must be 'kg' or 'lb'.")

    weight = float(input("Enter patient weight: "))
    dose_per_kg = float(input("Enter prescribed dose (mg/kg): "))

    if weight <= 0:
        raise ValueError("Weight must be greater than zero.")

    if dose_per_kg <= 0:
        raise ValueError("Dose must be greater than zero.")

    if unit == "lb":
        weight_kg = convert_lbs_to_kg(weight)
    else:
        weight_kg = weight

    if weight_kg < 0.5 or weight_kg > 300:
        raise ValueError("Weight appears outside a reasonable clinical range.")

    total_dose = calculate_dose(weight_kg, dose_per_kg)

    print()
    print("Medication Dose Summary")
    print("-" * 30)
    print(f"Original weight: {weight:.2f} {unit}")
    print(f"Weight in kg: {weight_kg:.2f} kg")
    print(f"Prescribed dose: {dose_per_kg:.2f} mg/kg")
    print(f"Total dose: {total_dose:.2f} mg")

    if total_dose > 1000:
        print("Warning: Total dose exceeds 1000 mg. Verify against medication-specific dosing limits.")

except ValueError as error:
    print()
    print(f"Error: {error}")