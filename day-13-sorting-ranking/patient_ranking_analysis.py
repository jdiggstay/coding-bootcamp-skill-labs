import pandas as pd

data = {
    "name": ["Anna", "Benjamin", "Carol", "Donald", "Evelyn"],
    "age": [43, 51, 27, 64, 48],
    "bmi": [23.4, 32.1, 21.2, 29.8, 35.4]
}

df = pd.DataFrame(data)

# Sort by BMI descending
df["bmi_rank"] = range(1, len(df) + 1)

print("Patient BMI Ranking")
print(df)
