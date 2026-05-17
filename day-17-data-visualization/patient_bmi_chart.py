import pandas as pd
import matplotlib.pyplot as plt

data = {
    "name": ["Anna", "Benjamin", "Carol", "Donald", "Evelyn"],
   "bmi": [23.4, 32.1, 21.2, 29.8, 35.4]
}

df = pd.DataFrame(data)

df.plot(kind="bar", x="name", y="bmi", legend=False)

plt.title("Patient BMI Comparison")
plt.ylabel("BMI")
plt.tight_layout()

plt.savefig("patient_bmi_chart.png")
plt.show()