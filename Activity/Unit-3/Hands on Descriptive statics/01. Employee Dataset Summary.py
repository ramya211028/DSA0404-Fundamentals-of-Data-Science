import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 28, 35],
    "Salary": [50000, 60000, None, 70000],
    "Department": ["HR", "IT", "Finance", "IT"]
}
df = pd.DataFrame(data)
print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nStatistical Summary:")
print(df.describe(include='all'))
