thisdist = {
    'car': "Ford",
    "modal": 1997,
    "working": True,
}

print(thisdist['car'])
print(thisdist.get('modal'))
x = thisdist.keys()
print(thisdist.keys(), x)
y = thisdist.values()
print(thisdist.values(), y)
z = thisdist.items()
print(thisdist.items(), z)
# print(thisdist.fromkeys())
thisdist['color'] = 'grey'
print(x, thisdist)
thisdist['color'] = 'yellow'
print(y, thisdist)
thisdist['year'] = 2020
print(y, thisdist)
thisdist['version'] = 2.0
print(z, thisdist)

if 'car' in thisdist:
    print("yes, 'car' is one of the keys in the thisdist dictionary")