print("Patient Registry Manager")

patients = []

for i in range(3):
    print(f"\nEnter patient #{i +1}")

    name = input("Name: ")
    age = int(input("Age: "))
    bmi = float(input("BMI: "))

    patient = {
        "name": name,
        "age": age,
        "bmi": bmi
    }

    patients.append(patient)

print("\nPatient Summary")
print("-" * 30)

for patient in patients:
    print(
        f"{patient['name']}: "
        f"Age {patient['age']}, "
        f"BMI {patient['bmi']:.1f}"
    )