thisset = {True, 'apple', 'banana', 'rr', 'Orange', 'x', 23, 'va', 'tt', 'ww', 'cherry', 'y'}

thisset.remove('y')
print(thisset)
thisset.pop()
print(thisset)
thisset.discard('ww')
print(thisset)

print(thisset.clear())
print(thisset)

thisset = {True, 'apple', 'banana', 'rr', 'Orange', 'x', 23, 'va', 'tt', 'ww', 'cherry', 'y'}

print(thisset)
del thisset

print(thisset)