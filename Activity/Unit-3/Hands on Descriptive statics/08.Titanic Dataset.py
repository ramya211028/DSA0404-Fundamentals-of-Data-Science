import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Titanic-Dataset.csv")
print("Dataset Information")
print(df.info())
print("\nMissing Values")
print(df.isnull().sum())
print("\nDescriptive Statistics")
print(df.describe())
df.hist(figsize=(10,8))
plt.show()
numeric_cols = ["Age", "Fare"]
for col in numeric_cols:
    plt.figure()
    df.boxplot(column=col)
    plt.title(col)
    plt.show()
Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
clean_df = df[(df["Age"] >= lower) & (df["Age"] <= upper)]
print("\nCleaned Dataset")
print(clean_df)
clean_df.to_csv("Titanic_Cleaned.csv", index=False)

print("\nCleaned dataset saved as Titanic_Cleaned.csv")
