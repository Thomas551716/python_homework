#Task 1: Hello Function 

def hello():
    return "Hello"
print(hello())

#Task 2: Greet function

def greet (name):
    return f"Hello, {name}! how are you today?"
print(greet("Kingtom"))



#Task 3: Calculater function

def calc(a, b, operation = "multiply"):
    try:
        match operation:
            case "add":
                return a + b 
            case "sutract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b 
            case "int-divide":
                return a //b
            case "power":
                return a ** b 
    except ZeroDivisionError:
        return " you can't divide by 0!"
    except TypeError:
        return " Invalid "
        
print(calc(5, 3, "add"))
print(calc(8, 2, "sutract"))       
print(calc(6, 3, "multiply"))       
print(calc(8, 3, "divide"))
print(calc(10, 3, "modulo"))
print(calc(9, 3, "int-divide"))
print(calc(5, 3, "power"))"

#Task 4: Data Type Conversion

def dp_conversion(value, data_type):
    try:
        if data_type == 'float':
            return float(value)
        elif data_type == 'str':
            return str(value)
        elif data_type == 'int':
            return int(value)
    except (ValueError,TypeError):
        return f" can not Covert {value} into a {data_type}."
    
print (dp_conversion("123.45", "float:"))
print (dp_conversion("123.45", "str"))
print (dp_conversion("Hello ", "int"))    
print (dp_conversion("Hi", "float"))
print (dp_conversion("123.45", "float:"))
#Task 5: Grading System using *args

def grade(*args):
    try:
        #check if the arguments are numbers
        if not all(isinstance(arg, (int, float)) for arg in args):
            return "Invalid Data"
        #calculate the average of the grades
        average = sum(args) / len(args)

        # grades based on the average
        if average >= 90:
            return "A"
        elif average >=80:
            return "B"
        elif average >=70:
            return "C"
        elif average >=60:
            return "D"
        else:
            return "F"
    except ZeroDivisionError:
        return "Incomplete or No Grade"
    
print (grade(99, 88, 97))
print (grade(56))
        
# Task 6: For loop with a Range
def repeat (string, count):
    result = ""
    for _ in range (count):
        result += string 
    return result

print(repeat ("Hold on ", 3))

# Task 7: Student Scores using **Kwargs
def student_scores (mode, **kwargs):
    if not kwargs:
        return " unavailable" 
    # Return unknown if no scores are given
    if mode == "best":
        return max(kwargs, key=kwargs.get) 
    # Get the student with the highest score
    elif mode == "mean":
        return sum(kwargs.values())/ len(kwargs)
    # calculate the average score

print(student_scores("best", thomas=90, tammy=57, tummy=89))
print(student_scores("mean", thomas=90, tammy=57, tummy=89))

# Task 8: Titleize, with string and list operation
def titleize(text):
    few_words = {"a","on","an","the","of","in","and","is"}
    words = text.lower().split() 
    #convert these few word into lowercase and split into words

    for i, word in enumerate(words):
        # Capitalize the first and last word, or words not in the few_words set
        if i == 0 or i==len(words) - 1 or word not in few_words:
            words[i] = word.capitalize()
    return " ".join(words)
    # join words back into a string

print (titleize("tom and jerry"))
print (titleize("a mice and men"))
print (titleize("holly bible "))

# Task 9: Hangman, with more String Operation 
def hangman(secret, guess):
    return "".join(letter if letter in guess else "~" for letter in secret)

print (hangman("alphabet", "ab"))
print (hangman("tomandjerry", "qrstuv"))"

# Task 10: Pig Latin function, string manipulation exercise Pig latin is akid's trick language.
def pig_latin(text):
    vowels = "aeiou"
    words = text.split() # spit the sentenses into words
    pig_latin_words=[]

    for word in words:
        if word[0] in vowels:
            pig_latin_word = word + "ay"
        elif word.startswith("qu"):
            pig_latin_word = word[2:] + "quay"
        else:
            consonant_cluster = ""
            for char in word:
                if char in vowels:
                    break
                consonant_cluster += char
            pig_latin_word = word[len(consonant_cluster):] + consonant_cluster + "ay"

        pig_latin_words.append(pig_latin_word)

    return " ".join(pig_latin_words)

print (pig_latin("apple"))
print (pig_latin("elephant"))
print (pig_latin("python"))
print (pig_latin("orange"))
print (pig_latin("the quick fox"))