# Task 2. Read a CSV File(read_emplyee function)

import datetime
import csv
from custom_module import some_function
import os
import sys

def read_employees():
    employees_data = {"fields": [], "rows":[]}

    try:
        with open("employees.csv", newline='', encoding= "utf-8") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    employees_data["fields"] = row
                else:
                    employees_data["rows"].append(row)
        return employees_data
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

#Global variable
employees = read_employees()

# Print for verification 
print(employees)


# Task 3 . Find the Column index (column_index function)

def column_index(column_name):
    try:
        return employees["fields"].index(column_name)
    except ValueError:
        print(f"column '{column_name}' not found.")
        return -1 # Indicating column not found

# Store column index for employee_id
employee_id_column = column_index("employee_id")

# Task 4 . Find the Employee First Name (first_name function)

def first_name(row_number):
    first_name_col = column_index("first_name")
    if first_name_col == -1:
        return None # Column not found
    try:
        return employees["rows"][row_number][first_name_col]
    except IndexError:
        print(f"Row {row_number} is out of range.")
        return None
    
# Task 5. Find the Employee (function in a function)
def empolyee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == empolyee_find
    matches = list (filter(employee_match, employees["rows"]))
    return matches

#Task 6. Find the Employee with a Lambda

def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

#Task 7. Sort by Last Name Using a Lambda

def sort_by_last_name():
    last_name_col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_col])
    return employees["rows"]

# Call the sorting function and print the result
sort_by_last_name()
print(employees) # print the dictionary to see the sorted output

#Task 8. Create a Dict for an Employee

def employee_dict(row):
    """Converts a row into a dictionary, excluding the employee_id field."""
    headers = employees["fields"]
    employee_id_col = column_index("employee_id") # Get employee_id column index

    # Create a dictionary using zip(), but exclude the employee_id_column
    employee_data = {headers[i]: row[i] for i in range(len(headers)) if i != employee_id_col}

    return employee_data

# Test with the first row in employee["rows"]
print(employee_dict(employees["rows"][0]))

#Task 9. Create a Dict of Dicts for All Employees

def all_employee_dict():
    """Creates a dictionary of all employees with employee_id as key."""
    employee_id_col = column_index("employee_id") # Get employee_id column index

    # Use dictionary comprehension to create the dict
    all_employeees = {int(row[employee_id_col]):employee_dict(row) for row in employees["rows"]}

    return all_employeees


# test the function and print the result 
print(all_employee_dict())

#Task 10. Use the Os module


def get_this_value():
     """Return the value of the THISVALUE environment variable."""
     return os.getenv("THISVALUE")

# Test the function
print(get_this_value())

#Task 11. Creating your own module


def set_that_secret(new_secret):
    """Sets the secret value in the custome_module."""
    custom_module.set_secret(new_secret)

#Test the function
set_that_secret("new_secret_value")
print(custom_module.secret) # should print " new_secret_value"

#Task 12. Read minutes1.csv and minutes2.csv

def read_minutes():
    """Reads minutes1.csv and minutes2.csv, storing rows as tuples."""
    def read_file(filename):
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                fields = next(reader) #First row as headers
                rows = [tuple(row) for row in reader] #convert rows to tuples
                return {"fields": fields, "rows": rows}
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
            return {"fields": [], "rows": []}
    return read_file("minutes1.csv"), read_file("minutes2.csv")

#Store results globally
minutes1, minutes2 = read_minutes()
print(minutes1, minutes2)

#Task 13. Create minutes_set

def create_minutes_set():
    """Creates a set of unique meeting records from minutes1 and minutes2."""
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1 | set2 # Union of both sets

# Store globally
minutes_set = create_minutes_set()
print(minutes_set)

#Task 14. Convert to datetime

def create_minutes_list():
    """Converts minutes_set to a sorted list with datetime objects."""
    minutes_list = list(minutes_set) #convert set to list
    #Convert date string to datetime object
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return minutes_list

#Store globally 
minutes_list = create_minutes_list()
print(minutes_list)

#Task 15 . Write out sorted list

def write_sorted_list():
    """ Sorts minutes_list and writes it to minutes.csv."""
    global minutes_list
    #Sort by the second element (date)
    minutes_list.sort(key=lambda x: x[1])

    #Convert datetime back to string format
    formatted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))
    
    #Write to CSV
    with open("minutes.csv", "w", newline= "")as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"]) # Write headers
        writer.writerows(formatted_list) #Write rows
    return formatted_list

# Call function
write_sorted_list()
print("Sorted minutes written to minutes.csv")