x = None
print(x)
print(type(x))
print(type(x) == None)

if not x is None:
    print("Not None")
elif x is None:
    print("None")
else:
    print("Nothing")

if x is not None:
    print("Not None")
elif x is None:
    print("None")
else:
    print("Nothing")

print(bool(None))

def func():
    b = 2

print(func())
