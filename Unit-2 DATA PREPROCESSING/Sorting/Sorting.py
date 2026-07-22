import pandas as pd
data = {
    'Name': ['Arun', 'Bala', 'Chitra', 'Divya', 'Ezhil', 'Fathima'],
    'Department': ['CSE', 'ECE', 'CSE', 'ECE', 'CSE', 'ECE'],
    'Marks': [85, 78, 92, 88, 75, 95]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)
sorted_df = df.sort_values(by='Marks', ascending=False)
print("\nSorted Data (Highest Marks First):")
print(sorted_df)
