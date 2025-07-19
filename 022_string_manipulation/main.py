text = 'String manipulation'

print(text[1])                  # Prints the second character (index starts at 0): 't'
print(text[1:5])                # Prints characters from index 1 to 4: 'trin'
print(text[1:5:8])              # Prints every 8th character from index 1 to 4 (only 1 character here): 't'
print(text[:5])                 # Prints the first 5 characters: 'Strin'
print(text[7:])                 # Prints from index 7 to the end: 'manipulation'
print(text[1::4])               # Prints every 4th character starting from index 1: 'tgpai'

print(len(text))                # Prints the total length of the string: 19
print(text.count('a'))          # Counts how many times 'a' appears in the entire string: 2
print(text.count('a', 0, 10))   # Counts 'a' only from index 0 to 9: 1

print(text.find('ni'))          # Returns the index where 'ni' first appears: 4
print(text.find('nix'))         # Returns -1 because 'nix' is not found in the string

print('String' in text)         # Checks if 'String' is a substring of text: True
print(text.replace('String', 'Text'))  # Replaces 'String' with 'Text': 'Text manipulation'

print(text.upper())             # Converts the entire string to uppercase
print(text.lower())             # Converts the entire string to lowercase
print(text.capitalize())        # Capitalizes the first letter only: 'String manipulation'
print(text.title())             # Capitalizes the first letter of each word: 'String Manipulation'

print(text.strip())             # Removes whitespace from both ends (none in this case)
print(text.rstrip())            # Removes whitespace from the right side
print(text.lstrip())            # Removes whitespace from the left side

print(text.split())             # Splits the string into a list of words: ['String', 'manipulation']
print('#'.join(text))           # Joins each character with '#' between them
