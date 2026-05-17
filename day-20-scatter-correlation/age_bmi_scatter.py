import pandas as pd
import matplotlib.pyplot as plt

data = {
    "age": [29, 35, 42, 48, 52, 61, 67],
    "bmi": [22.1, 24.8, 26.4, 29.1, 31.2, 33.5, 34.8]
}

df = pd.DataFrame(data)

# Calculate correlation
correlation = df["age"].corr(df["bmi"])
print(f"Correlation between age and BMI: {correlation:.2f}")

# Create scatter plot
df.plot(
    kind="scatter",
    x="age",
    y="bmi",
    figsize=(8, 5)
)

plt.title("Age vs BMI")
plt.xlabel("Age")
plt.ylabel("BMI")
plt.grid(True)
plt.tight_layout()

plt.savefig("age_bmi_scatter.png")
plt.show()