import pandas as pd



# Task 1.1 Creating a DataFrame from Dictionary

data = {

    "Name": ["Alice", "Bob", "Charlie"],

    "Age": [25, 30, 35],

    "City": ["New York", "Los Angeles", "Chicago"]

}

     # Convert dictionary to DataFrame using Pandas.

task1_data_frame = pd.DataFrame(data)

     # Print to verify

print("Task 1 - Original DataFrame:")

print(task1_data_frame)

     # Task 1.2 Add a new Column
     # Make a copy of the DataFrame

task1_with_salary = task1_data_frame.copy()

     # Add the 'Salary' column

task1_with_salary["Salary"] = [70000, 80000, 90000]

     # Print to verify

print("\nTask 1.2 - DataFrame with Salary Column:")

print(task1_with_salary)

     # Task1.3 Modifying the Column
     # Make a copy of the DataFrame

task1_older = task1_with_salary.copy()

     # Increment the 'Age' column by 1

task1_older["Age"] += 1

     # Print to verify

print("\nTask 1.3 - DataFrame with Incremented Age:")

print(task1_older)

     # Save to CSV file without index

task1_older.to_csv("employees.csv", index=False)

     # Verify CSV content by reading it back

df_from_csv = pd.read_csv("employees.csv")

print("\nTask 1.4 - Contents of the Saved CSV File:")

print(df_from_csv)

# Task 2 Loading Data from CSV and JSON

import pandas as pd

     # Load the CSV file from Task 1 into a new DataFrame

task2_employees = pd.read_csv("employees.csv")

     # Print to verify contents

print("Task 2.1 - Data from CSV:")

print(task2_employees)

import json

     # Create data for additional employees

additional_employees = [

    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},

    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}

]

     # Save JSON data to a file

with open("additional_employees.json", "w") as json_file:

    json.dump(additional_employees, json_file, indent=4)

     # Read JSON file into a DataFrame

json_employees = pd.read_json("additional_employees.json")

     # Print to verify

print("\nTask 2.2 - Data from JSON:")

print(json_employees)

    # Combine the CSV and JSON DataFrames

more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
     # Print the combined DataFrame

print("\nTask 2.3 - Combined DataFrame:")

print(more_employees)

# Task 3 Data Inspection using Head(),Tail() and info()

     # Get the first three rows

first_three = more_employees.head(3)

     # Print to verify

print("Task 3.1 - First Three Rows:")

print(first_three)

     # Get the last two rows

last_two = more_employees.tail(2)

     # Print to verify

print("\nTask 3.2 - Last Two Rows:")

print(last_two)

     # Get the shape (rows, columns)

employee_shape = more_employees.shape

     # Print the shape

print("\nTask 3.3 - Shape of DataFrame:")

print(employee_shape)

     # Print concise summary

print("\nTask 3.4 - DataFrame Info:")

more_employees.info()

# Task 4 Data Cleaning

     # Load dirty data from CSV

dirty_data = pd.read_csv("dirty_data.csv")

     # Print to verify

print("\nTask 4.1 - Dirty Data:")

print(dirty_data)

     # Make a copy for cleaning

clean_data = dirty_data.copy()

     # Remove duplicates

clean_data = clean_data.drop_duplicates()

     # Print to verify

print("\nTask 4.2 - After Removing Duplicates:")

print(clean_data)

     # Remove duplicates

clean_data = clean_data.drop_duplicates()

     # Print to verify

print("\nTask 4.2 - After Removing Duplicates:")

print(clean_data)

     # Replace placeholders with NaN

clean_data["Salary"] = clean_data["Salary"].replace(["unknown", "n/a"], pd.NA)

     # Convert to numeric

clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")

     # Print to verify

print("\nTask 4.4 - Salary Cleaned and Converted:")

print(clean_data)

     # Fill missing 'Age' with mean

clean_data["Age"].fillna(clean_data["Age"].mean(), inplace=True)

     # Fill missing 'Salary' with median

clean_data["Salary"].fillna(clean_data["Salary"].median(), inplace=True)

     # Print to verify

print("\nTask 4.5 - Missing Numeric Values Filled:")

print(clean_data)

     # Fill missing 'Age' with mean

clean_data["Age"].fillna(clean_data["Age"].mean(), inplace=True)

     # Fill missing 'Salary' with median

clean_data["Salary"].fillna(clean_data["Salary"].median(), inplace=True)

     # Print to verify

print("\nTask 4.5 - Missing Numeric Values Filled:")

print(clean_data)

     # Strip whitespace and convert to uppercase

clean_data["Name"] = clean_data["Name"].str.strip().str.upper()

clean_data["Department"] = clean_data["Department"].str.strip().str.upper()

     # Print to verify

print("\nTask 4.7 - Standardized Name and Department:")

print(clean_data)

