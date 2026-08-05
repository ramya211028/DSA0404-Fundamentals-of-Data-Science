import pandas as pd
sales = [100,120,130,125,128,140,135,138,500]
df = pd.DataFrame({"Sales": sales})
Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
clean_df = df[(df["Sales"] >= lower) & (df["Sales"] <= upper)]
print("Original Dataset")
print(df)
print("\nCleaned Dataset")
print(clean_df)
