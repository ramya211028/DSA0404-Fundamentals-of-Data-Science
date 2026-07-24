import pandas as pd
df = pd.DataFrame({
    "Name": ["John", "Emma", "Liam", "Olivia"],
    "Age": [20, 19, 21, 18],
    "Student": [True, True, False, True]
})
new_row = pd.DataFrame([{
    "Name": "Sophia",
    "Age": 22,
    "Student": False
}])
df = pd.concat([df, new_row], ignore_index=True)
print(df)
