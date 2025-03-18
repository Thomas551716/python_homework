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