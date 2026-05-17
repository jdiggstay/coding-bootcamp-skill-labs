import pandas as pd

data = { 
    "name": ["Anna", "Benjamin", "Carol", "Donald"],
    "bmi": [23.4, None, 21.2, 29.8],
    "age": [43, 51, None, 64]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

print("\nMissing Values by Column")
print(df.isnull().sum())

print("\nFill Missing BMI with Average")
df["bmi"] = df["bmi"].fillna(df["bmi"].mean())

print("\nFill Missing Age with Average")
df["age"] = df["age"].fillna(df["age"].mean())

print("\nCleaned Data")
print(df)