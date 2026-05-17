import pandas as pd

data = {
    "name": ["Anna", "Benjamin", "Carol", "Donald"],
    "age": [43, 51, 27, 64],
    "bmi": [23.4, 32.1, 21.2, 29.8]
}

df = pd.DataFrame(data)

print("Patient Data")
print(df)

print("\nSummary Statistics")
print(df.describe())

print("\nPatients with BMI >= 30")
print(df[df["bmi"] >= 30])