import pandas as pd
import matplotlib.pyplot as plt
salary = [25000,28000,30000,32000,35000,36000,38000,100000]
df = pd.DataFrame({"Salary": salary})
df.boxplot(column="Salary")
plt.title("Salary Box Plot")
plt.show()
print("Outliers can be identified from the box plot.")
