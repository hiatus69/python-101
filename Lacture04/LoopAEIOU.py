input_string = input("Please enter a string: ")

modified_string = ""

vowel = "AEIOU"

for char in input_string:
    
    upper_char = char.upper()
    modified_string += "*"
    
    if upper_char in vowel:
        modified_string += upper_char

print("Modified string:", modified_string)