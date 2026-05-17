import pandas as pd

# Load the CSV file
df = pd.read_csv("patients.csv")

print("Patient Data")
print(df)

print("\nSummary Statistics")
print(df.describe())

print("\nHigh-Risk Patients (BMI >= 30)")
print(df[df["bmi"] >= 30])

print("\nAverage BMI")
print(df["bmi"].mean())
