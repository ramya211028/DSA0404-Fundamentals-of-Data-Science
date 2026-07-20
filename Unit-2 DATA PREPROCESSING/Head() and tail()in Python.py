import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'Score': [85, 92, 78, 95, 88, 72, 91]
}
df = pd.DataFrame(data)
print(df.head())
print(df.head(2))
print(df.tail(3))
