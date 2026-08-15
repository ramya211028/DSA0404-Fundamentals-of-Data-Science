import pandas as pd
import matplotlib.pyplot as plt
prices = [120000,150000,180000,200000,250000,300000,350000,400000,800000]
df = pd.DataFrame({"House Price": prices})
df["House Price"].plot(kind="hist", bins=5)
plt.title("House Price Distribution")
plt.xlabel("Price")
plt.show()
print("Observe the histogram to determine whether the data is normally distributed or skewed.")
