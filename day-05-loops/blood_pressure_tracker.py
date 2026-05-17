print("Blood Pressure Tracker")

readings = []

for i in range(3):
    systolic = int(input(f"Enter systolic reading #{i + 1}: "))
    readings.append(systolic)

average = sum(readings) / len(readings)

print()
print(f"Readings: {readings}")
print(f"Average systolic pressure: {average:.1f} mmHg")

if average >= 140:
    category = "High Blood Pressure Stage 2"
elif average >= 130:
    category = "High Blood Pressure Stage 1"
elif average >= 120:
    category = "Elevated"
else:
    category = "Normal"

print(f"Classification: {category}")