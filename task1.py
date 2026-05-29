import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load the dataset
# Ensure 'insurance.csv' is in your VS Code project folder
df = pd.read_csv('insurance.csv')

# 2. Data Cleaning
print("--- Initial Data Info ---")
print("Statistics Information")
print(df.info())

# Handle Missing Values (if any)
# Note: This dataset is usually clean, but we include this for your internship task requirement
df.fillna(df.median(numeric_only=True), inplace=True) 

# Remove Duplicates
duplicate_count = df.duplicated().sum()
print(f"\nRemoving {duplicate_count} duplicate rows...")
df.drop_duplicates(inplace=True)

# 3. Processing
# Check for outliers in 'bmi' using a boxplot logic
Q1 = df['bmi'].quantile(0.25)
Q3 = df['bmi'].quantile(0.75)
IQR = Q3 - Q1
print(f"Interquartile Range: {IQR}")
print("Statistics completed")

# 4. Data Visualization
plt.figure(figsize=(15, 5))

# Plot 1: Age Distribution (Histogram)
plt.subplot(1, 3, 1)
sns.histplot(df['age'], kde=True, color='blue')
plt.title('Age Distribution')

# Plot 2: Charges by Smoker Status (Bar Plot)
plt.subplot(1, 3, 2)
sns.barplot(x='smoker', y='charges', data=df, palette='viridis')
plt.title('Medical Charges: Smoker vs Non-Smoker')

# Plot 3: BMI vs Charges (Scatter Plot)
plt.subplot(1, 3, 3)
sns.scatterplot(x='bmi', y='charges', hue='smoker', data=df)
plt.title('BMI vs Charges')

plt.tight_layout()
plt.show()

# 5. Summary Findings
print("\n--- Key Insights ---")
print(f"Total records processed: {len(df)}")
print("Insight: Smoking has a massive impact on medical charges compared to BMI alone.")