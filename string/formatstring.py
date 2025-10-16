# String concatenation in Python
x = 'hello'
y = 'world'
z = x + ' ' + y
print(z)  # Output: hello world
print(x+y)

#formatting strings
val = 'hello world'
print(f'{val} wellcome to python')  # Using f-string for formatting

price = 49
txt = f"the price of bottle is {price}"
print(txt)

quantity = 3
bottle = f'the total bottles price is {quantity * price:.2f}'  # Formatting to 2 decimal places
print(bottle)

total = quantity * price
print(f'the quanity of bottols is {total/price:.2f}')

# Using format method for formatting
txt1 = 'the price of bottle is {}'
print(txt1.format(price))

txt2 = 'the price of bottle is {} and the quantity is {}'
print(txt2.format(price, quantity))
txt3 = 'the price of bottle is {p:.2f} and the quantity is {q}'
print(txt3.format(q=quantity, p=price))

# Using % operator for formatting
txt4 = 'the price of bottle is %d and the quantity is %d' %(price, quantity)
print(txt4)
print(f'{x} wellcome'.format(x))

# Using %s for string formatting
name = 'sathish'
txt5 = 'hello, %s' % name
print(txt5)
# Using %f for float formatting
price1 = 49.99
txt6 = 'the price of bottle is %.2f' % price1  # Formatting to 2 decimal places
print(txt6)

# Using %r for representation
txt7 = 'the price of bottle is %r' % price1
print(txt7)
# Using %x for hexadecimal formatting
num = 255
txt8 = 'the hexadecimal representation of %d is %x' % (num, num)
print(txt8)