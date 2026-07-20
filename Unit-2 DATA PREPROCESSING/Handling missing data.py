import pandas as pd
import numpy as np
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, np.nan, 30, 22],
    'Salary': [50000, 60000, np.nan, 45000]
}
df = pd.DataFrame(data)
print("Missing count:\n", df.isnull().sum())
df['Age'] = df['Age'].fillna(df['Age'].median())
df = df.dropna(subset=['Salary'])
print("\nCleaned DataFrame:\n", df)
