import pandas as pd

data = {
   "name": ["Anna", "Benjamin", "Carol", "Donald", "Evelyn"],
    "age": [43, 51, 27, 64, 48],
    "bmi": [23.4, 32.1, 21.2, 29.8, 35.4]
}

df = pd.DataFrame(data)

# Create risk category
df["bmi_category"] = df["bmi"].apply(
    lambda bmi: "Obesity" if bmi >= 30 else "Non-Obesity"
)

# Group and summarize
summary = df.groupby("bmi_category").agg({
    "name": "count",
    "age": "mean",
    "bmi": "mean"
})

# Rename columns for clarity
summary = summary.rename(columns={
    "name": "patient_count",
    "age": "average_age",
    "bmi": "average_bmi"
})

print("Patient Summary by BMI Category")
print(summary)
