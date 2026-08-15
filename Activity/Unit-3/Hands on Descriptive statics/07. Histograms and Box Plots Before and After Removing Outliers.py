import pandas as pd
import matplotlib.pyplot as plt
data = [12,15,18,20,22,25,27,29,30,100]
df = pd.DataFrame({"Values": data})
Q1 = df["Values"].quantile(0.25)
Q3 = df["Values"].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
clean_df = df[(df["Values"] >= lower) & (df["Values"] <= upper)]
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
df["Values"].plot(kind="hist", title="Before Removing Outliers")
plt.subplot(1,2,2)
clean_df["Values"].plot(kind="hist", title="After Removing Outliers")
plt.show()
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
df.boxplot(column="Values")
plt.subplot(1,2,2)
clean_df.boxplot(column="Values")
plt.show()
