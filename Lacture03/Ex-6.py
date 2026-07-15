# program to compare two strings

string1 = "Mary"
string2 = "Merk"

# compare the strings for equality
if string1 == string2:
    print(f'"{string1}" and "{string2}" are equal.')
else:
    print(f'"{string1}" and "{string2}" are not equal.')
    
# compare the strings for lexicographical order    
if string1 < string2:
    print(f'"{string1}" come before "{string2}" in lexicographical order.')
elif string1 > string2:
    print(f'"{string1}" come after "{string2}" in lexicographical order.')
   
# compare the strings for equality ignoring case    
if string1.lower() == string2.lower():
    print(f'"{string1}" and "{string2}" are equal when case is ignored.')
else:
    print(f'"{string1}" and "{string2}" are not equal when case is ignored.')