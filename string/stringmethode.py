    # The above code demonstrates various string operations in Python:
    # - Printing strings with single and double quotes.
    # - Handling quotes inside strings.
    # - Assigning strings to variables.
    # - Using triple quotes for multi-line strings.
    # - Accessing characters in a string by index.
    # - Iterating over each character in a string using a for loop.
    # - Getting the length of a string with len().
    # - Checking for substring presence using 'in' and 'not in'.
    # - Using conditional statements to print messages based on substring checks.
print("Hello, World!")
print('Hello, World!')
print("I' am Sathish")
print('"I" am Sathish')

x = 'hello world'
print(x)

y = '''kjsdhkjskfjlkslk
sfjkhfkskfjlksjf
sfklskfhkjnfskn
sdkjnskfksnf'''
print(y)

#or
z = """kjsdhkjskfjlkslk
sfjkhfkskfjlksjf
sfklskfhkjnfskn
sdkjnskfksnf"""
print(z)

print(y[10]) #empty string


for i in "banana":
    print(i)

print(len(y)) #length of string

print('hello' in x)

txt = "The best things in life are free!"

if 'free' in txt:
    print("Yes, 'free' is present.")

print('hello' not in x)

if 'hello' not in txt:
    print("No, 'hello' is NOT present.")
