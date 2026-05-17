import pandas as pd

import matplotlib.pyplot as plt

data = {
    "age": [29, 35, 42, 48, 52, 61, 67],
    "bmi": [22.1, 24.8, 26.4, 29.1, 31.2, 33.5, 34.8],
    "systolic_bp": [110, 118, 122, 130, 136, 142, 148]
}

df = pd.DataFrame(data)

# Calculate correlation matrix
corr = df.corr()
print("Correlation Matrix")
print(corr)

# Create heatmap
plt.figure(figsize=(6,5))
plt.imshow(corr, aspect="auto")
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Patient Correlation Matrix")
plt.tight_layout()

plt.savefig("patient_correlation_matrix.png")
plt.show()