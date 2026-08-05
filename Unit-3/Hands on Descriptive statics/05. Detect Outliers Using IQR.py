import pandas as pd
marks = [45,50,55,60,62,65,67,70,72,150]
df = pd.DataFrame({"Marks": marks})
Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df["Marks"] < lower) | (df["Marks"] > upper)]
print("Outliers:")
print(outliers)
