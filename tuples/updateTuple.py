x = ("apple", "banana", "apple", "cherry")
print(x)
y = list(x)
y[0] = 'eeee'
y.append('555')
y.insert(2, 'jnkjnfdk')
print(y)
x = tuple(y)
print(x)

z = x+('44',)
print(z)

y.pop()
print(y)
y.remove("apple")

x = tuple(y)
print(x)
del x

# print(x)
