a = 'wellcome, to python'

print(a.title())              # Capitalizes the first letter of each word
print(a.upper())              # Converts all characters to uppercase
print(a.lower())              # Converts all characters to lowercase
print(a.capitalize())         # Capitalizes the first character
print(a.swapcase())           # Swaps case of all characters
print(a.casefold())           # Aggressive lowercasing for caseless matching
print(a.center(30, '-'))      # Centers string with padding
print(a.count('o'))           # Counts occurrences of substring
print(a.encode())             # Encodes string to bytes
print(a.endswith('python'))   # Checks if string ends with substring
print(a.expandtabs(4))        # Expands tabs to spaces
print(a.find('to'))           # Finds substring, returns lowest index or -1
print(a.format())             # Formats string
print(a.format_map({}))       # Formats using a mapping
print(a.index('to'))          # Finds substring, returns lowest index or raises ValueError
print(a.isalnum())            # Checks if all characters are alphanumeric
print(a.isalpha())            # Checks if all characters are alphabetic
print(a.isascii())            # Checks if all characters are ASCII
print(a.isdecimal())          # Checks if all characters are decimal
print(a.isdigit())            # Checks if all characters are digits
print(a.isidentifier())       # Checks if string is a valid identifier
print(a.islower())            # Checks if all cased characters are lowercase
print(a.isnumeric())          # Checks if all characters are numeric
print(a.isprintable())        # Checks if all characters are printable
print(a.isspace())            # Checks if all characters are whitespace
print(a.istitle())            # Checks if string is titlecased
print(a.isupper())            # Checks if all cased characters are uppercase
print(a.join(['Hello', 'World'])) # Joins iterable with string as separator
print(a.ljust(30, '-'))       # Left-justifies string with padding
print(a.lstrip())             # Removes leading whitespace
print(a.maketrans('o', '0'))  # Creates translation table
print(a.partition(','))       # Splits at first occurrence of separator
print(a.replace('o', '0'))    # Replaces substring with another
print(a.rfind('o'))           # Finds substring, returns highest index or -1
print(a.rindex('o'))          # Finds substring, returns highest index or raises ValueError
print(a.rjust(30, '-'))       # Right-justifies string with padding
print(a.rpartition(','))      # Splits at last occurrence of separator
print(a.rsplit())             # Splits string from the right
print(a.rstrip())             # Removes trailing whitespace
print(a.split())              # Splits string by whitespace
print(a.splitlines())         # Splits string at line breaks
print(a.startswith('well'))   # Checks if string starts with substring
print(a.strip())              # Removes leading and trailing whitespace
print(a.translate(str.maketrans('o', '0'))) # Translates characters
print(a.zfill(30))            # Pads string on the left with zeros

#string concatenation
a = 'hello'
b = 'world'
c = a + ' ' + b
print(c)                     # Output: hello world  
print(f'{a} {b}')            # Output: hello world using f-string
print('{} {}'.format(a,b))   # Output: hello world using format method
print(a.join(b))             # Output: whweolrllod (joins 'b' with 'a' as separator)    

