import pandas as pd
data = {
    'Name': ['Arun', 'Bala', 'Chitra', 'Divya', 'Ezhil', 'Fathima'],
    'Marks': [85, 78, 92, 88, 75, 95]
}
df = pd.DataFrame(data)
df['Rank'] = df['Marks'].rank(ascending=False, method='dense')
print("Students with Rank:")
print(df.sort_values(by='Rank'))
