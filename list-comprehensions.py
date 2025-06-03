# list-comprehensions.py
import pandas as pd
df = pd.read_csv("../csv/employees.csv")

# List of full names
names = [f"{row['first_name']} {row['last_name']}" for _, row in df.iterrows()]
print("All names:", names)

# Names containing 'e'
names_with_e = [name for name in names if 'e' in name.lower()]
print("Names with 'e':", names_with_e)