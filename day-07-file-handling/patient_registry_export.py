import csv

print("Patient Registry CSV Exporter")

patients = []

for i in range(3):
    print(f"\nEnter patient #{i + 1}")

    name = input("Name: ")
    age = int(input("Age: "))
    bmi = float(input("BMI: "))

    patients.append({
        "name": name,
        "age": age,
        "bmi": bmi    
        })
    
with open("patients.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "age", "bmi"])
    writer.writeheader()
    writer.writerows(patients)

print("\nData exported to patients.csv")