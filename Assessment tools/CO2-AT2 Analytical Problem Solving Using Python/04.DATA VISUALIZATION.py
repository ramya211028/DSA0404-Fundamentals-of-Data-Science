import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
raw_data = {
    "Employee_Name": [" Alice ", "Bob", "Charlie", "Diana", "Evan"],
    "Department": ["HR", "Engineering", "HR", "Engineering", "Marketing"],
    "Salary": [50000, 85000, np.nan, 92000, 60000],
    "Join_Date": [
        "2022-01-15",
        "2021-06-20",
        "2023-03-11",
        "2020-11-01",
        "2024-02-28",
    ],
}
df = pd.DataFrame(raw_data)
df["Employee_Name"] = df["Employee_Name"].str.strip()
median_salary = df["Salary"].median()
df["Salary"] = df["Salary"].fillna(median_salary)
df["Join_Date"] = pd.to_datetime(df["Join_Date"])
df["Years_of_Service"] = 2026 - df["Join_Date"].dt.year
dept_summary = (
    df.groupby("Department")
    .agg(
        Avg_Salary=("Salary", "mean"),
        Total_Employees=("Employee_Name", "count"),
    )
    .reset_index()
)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
axes[0].bar(
    dept_summary["Department"],
    dept_summary["Avg_Salary"],
    color=["skyblue", "orange", "green"]
)
axes[0].set_title("Average Salary by Department")
axes[0].set_xlabel("Department")
axes[0].set_ylabel("Salary ($)")
colors = {
    "HR": "red",
    "Engineering": "blue",
    "Marketing": "green"
}
for dept in df["Department"].unique():
    dept_data = df[df["Department"] == dept]
    axes[1].scatter(
        dept_data["Years_of_Service"],
        dept_data["Salary"],
        label=dept,
        s=100,
        color=colors[dept]
    )
axes[1].set_title("Salary vs. Years of Service")
axes[1].set_xlabel("Years of Service")
axes[1].set_ylabel("Salary ($)")
axes[1].legend()
plt.tight_layout()
plt.show()
