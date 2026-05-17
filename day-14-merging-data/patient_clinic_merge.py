import pandas as pd

patients = pd.DataFrame({
    "patient_id": [1, 2, 3],
    "name": ["Anna", "Benjamin", "Carol"],
    "bmi": [23.4, 32.1, 21.2]
    })

clinics = pd.DataFrame({
    "patient_id": [1, 2, 3],
    "clinic": ["Northside Clinic", "West End Clinic", "Downtown Clinic"]
})

merged = pd.merge(patients, clinics, on="patient_id")

print("Merged Patient and Clinic Data")
print(merged)