import pandas as pd
property_data = pd.read_csv("Expt.09 Data.txt")

avg_price = property_data.groupby("Location")["Listing Price"].mean()

more_than_4 = property_data[property_data["Bedrooms"] > 4]

largest_area = property_data.loc[property_data["Area"].idxmax()]

print("Average Listing Price by Location:")
print(avg_price)

print("\nNumber of properties with more than 4 bedrooms:", len(more_than_4))

print("\nProperty with Largest Area:")
print(largest_area)
