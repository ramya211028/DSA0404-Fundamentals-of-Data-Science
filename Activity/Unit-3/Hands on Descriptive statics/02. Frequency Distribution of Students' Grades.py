import pandas as pd
import matplotlib.pyplot as plt
grades = ["A","B","A","C","B","A","D","B","C","A","B","A"]
df = pd.DataFrame({"Grade": grades})
freq = df["Grade"].value_counts()
print(freq)
freq.plot(kind="bar")
plt.title("Frequency Distribution of Grades")
plt.xlabel("Grades")
plt.ylabel("Count")
plt.show()
