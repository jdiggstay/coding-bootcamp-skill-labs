import pandas as pd

data = {
    "name": ["Anna", "Benjamin", "Carol", "Donald"],
    "bmi": [23.4, None, 21.2, 29.8],
    "age": [43, 51, None, 64]
}

df = pd.DataFrame(data)

# Fill missing values
df["bmi"] = df["bmi"].fillna(df["bmi"].mean())
df["age"] = df["age"].fillna(df["age"].mean())

# Export cleaned data
df.to_csv("patients_cleaned.csv", index=False)

print("Cleaned patient data exported to patients_cleaned.csv")