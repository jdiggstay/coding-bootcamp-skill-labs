import pandas as pd
import matplotlib.pyplot as plt

data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "average_bmi": [28.5, 28.2, 27.9, 27.8, 27.6, 27.4]
}

df = pd.DataFrame(data)

df.plot(
    kind="line",
    x="month",
    y="average_bmi",
    marker="o",
    figsize=(8,5)
)

plt.title("Average Patient BMI Trend")
plt.ylabel("Average BMI")
plt.xlabel("Month")
plt.grid(True)
plt.tight_layout()

plt.savefig("patient_bmi_trend.png")
plt.show()