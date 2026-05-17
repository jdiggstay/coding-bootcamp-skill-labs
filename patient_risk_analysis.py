import pandas as pd

data = {
    "name": ["Anna", "Benjamin", "Carol", "Donald", "Evelyn"],
    "age": [43, 51, 27, 64, 48],
    "bmi": [23.4, 32.1, 21.2, 29.8, 35.4]
}

df = pd.DataFrame(data)

# Create calculated columns
df["high_risk"] = df["bmi"] >= 30
df["bmi_category"] = df["bmi"].apply(
    lambda bmi: "Obesity" if bmi >= 30 else "Non-Obesity"
)

print("Patient Risk Analysis")
print(df)

print("\nHigh-Risk Patients")
print(df[df["high_risk"]])

print("\nNumber of High-Risk Patients")
print(df["high_risk"].sum())