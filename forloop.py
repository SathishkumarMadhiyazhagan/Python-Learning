fruitslist = ['apple', 'banana', 'kiwi', 'manago']
fruitstuple = ('apple', 'banana', 'kiwi', 'manago')
fruitsset = {'apple', 'banana', 'kiwi', 'manago'}
fruitsdict = {'a':'apple', 'b':'banana', 'c':'kiwi', 'd':'manago'}

for x in fruitslist:
    print(x)

for x in fruitstuple:
    print(x)

for x in fruitsset:
    print(x)

for x in fruitsdict:
    print(fruitsdict[x])

for x in 'hello world':
    print(x)

for x in 'apple':
    if x=='e':
        break
    print(x)

for x in 'banana':
    if x == 'n':
        continue
    print(x)

for x in fruitslist:
    print(x)
else:
    print("Fruites List iteration using for loop completed")

for x in range(6):
    print(x)

for x in range(2, 6):
  print(x)

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("loop find 3 value")
print('hello')

for x in range(1, 30, 3):
  print(x)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass