is_student = True       
balance = 1000.75       
first_name = "Charlie"  
number_of_days = 7      

print(balance)
print("Done")

"""# Convert a string to an integer
num_str = "42"
num_int = int(num_str)  # 42 (integer)
print(num_int)

# Convert an integer to a float
num_float = float(num_int)  # 42.0 (float)
print(num_float)

# Convert a number to a string
num_str_again = str(num_int)  # "42" (string)
print(num_str_again)

# Convert to a Boolean
is_empty = not bool("")  # True 
is_non_zero = bool(5)  # True (non-zero numbers are considered True) 

age = 30
message = "I am " + str(age) + " years old."
print(message)

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

try:
    num = int(input("Enter a number: "))
except Exception as e:
    print(f"An error occurred: {e}")

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
else:
    print(f"Success! The result is {result}.")
try:
    file = open("example.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
finally:
    file.close()
    print("File closed.")
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
    return True

try:
    check_age(16)
except ValueError as e:
    print(e)
name = "Ed"
count = 6
kind_of_object = "apples"
print(f"{name} has {count} {kind_of_object}.") # Prints "Ed has 6 apples."
cost = 22/7
print(f"The pie cost ${cost:.2f}.")"""

"""def hello():
    return "Hello!"
    print(hello())"""

