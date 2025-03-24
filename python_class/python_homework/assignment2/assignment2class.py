"""# Mutable example (list)
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')  # We can add a new item
fruits[0] = 'orange'  # We can change an existing item
print(fruits)  # Now ['orange', 'banana', 'cherry', 'date']

# Immutable example (tuple)
colors = ('red', 'green', 'blue')
# colors[0] = 'yellow'  # This would cause an error
# You cannot change the tuple after creation

fruits = ['apple', 'banana', 'cherry']  # Define a list
fruits.append('orange')  # Add an item
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

    list_one = [3,4,5]
def incrementor(x):
    return x + 1

list_two = list(map(incrementor, list_one)) # [4,5,6]

list_one = [3,4,5]
list_two = list(map(lambda x: x+1, list_one)) # [4,5,6]

list_1 = ['A','B','C','D','E']
list_2 = list_1[1:3] # Slicing from beginning to end. Gives ['B','C'].  list_1[3] is not included.
list_3 = list_1[2:]  # Gives ['C','D','E']
list_4 = list_1[:2]  # Gives ['A', 'B']
list_5 = list_1[-2:] # Gives ['D', 'E'] -- the last two elements

dimensions = (1920, 1080)  # Define a tuple
print(dimensions[0])  # Access the first element: Output: 1920

person = {'name': 'Jazmine', 'age': 30}  # Define a dictionary
print(person['name'])  # Output: Jazmine
person['email'] = 'jazmine@example.com'  # Add a new key-value pair

unique_numbers = {1, 2, 3, 3, 4}  # Define a set (duplicates are ignored)
unique_numbers.add(5)  # Add a new item
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

with open('example.txt', 'r') as file:
    content = file.read()  # Read entire file
    print(content)

try:
    with open('example.txt', 'r') as file:
        content = file.read()  # Read entire file
        print(content)
except Exception as e:
    print(f"An error occurred reading the file: {e}")
else:
    print("The file was read ok.")

with open('example.txt', 'w') as file:
    file.write("Hello, World!")  # Write to the file


import csv

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])  # Write header row
    writer.writerow(['Jazmine', 30, 'New York'])  # Write a data row

# Import entire module
import math
print(math.sqrt(16))  # Output: 4.0

# Import specific functions
from math import sqrt
print(sqrt(16))  # Output: 4.0

# Use aliases for shorter names
import pandas as pd
df = pd.DataFrame({'Name': ['Jazmine', 'Luis'], 'Age': [30, 35]})

# math_tools.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# main.py
import math_tools
print(math_tools.add(2, 3))  # Output: 5



my_package/
    __init__.py         # Makes this directory a package
    math_tools.py       # Module for math operations
    string_tools.py     # Module for string operations
    

    # Import specific modules from a package
from my_package import math_tools
print(math_tools.add(10, 20))

# Import specific functions (if configured in __init__.py)
from my_package import add, multiply

external libraries for MOdule

pip install requests

# Then use in code:
import requests
response = requests.get('https://api.example.com/data')    
    

name = input("Enter your name: ")  # Displays a prompt and waits for input
print(f"Hello, {name}!")  # Greets the user with their input

age = input("Enter your age: ")  # Gets input as a string
age = int(age)  # Converts input to an integer
print(f"Next year, you will be {age + 1} years old.")

try:
    age = int(input("Enter your age: "))
    print(f"Next year, you will be {age + 1} years old.")
except ValueError:
    print("Please enter a valid number.")


    #working with OS
import os
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# Changing the Current Working Directory
os.chdir('/path/to/your/folder')
print(f"New working directory: {os.getcwd()}")

#The os.listdir() function returns a list containing all files and folders within the specified directory.

files = os.listdir('/path/to/your/folder')
print(f"Files in the directory: {files}")

#Creating and Removing Directories
# Create a new directory
os.mkdir('new_folder')

# Remove the directory
os.rmdir('new_folder')

#Checking if a Path Exists


if os.path.exists('some_file.txt'):
    print("The file exists.")
else:
    print("The file does not exist.")

#Getting File Information

if os.path.isfile('some_file.txt'):
    print("This is a file.")
elif os.path.isdir('some_folder'):
    print("This is a folder.")


#Install virtualenv (optional)
pip install virtualenv

#Create a Virtual Environment
python3 -m venv myenv

#Using virtualenv:

virtualenv myenv

#Activating the Virtual Environment

source myenv/Scripts/activate

#Installing Packages in the Virtual Environment
pip install requests

#Deactivating the Virtual Environment

deactivate
#Managing Dependencies with requirements.txt

pip freeze > requirements.txt
pip install -r requirements.txt

"""