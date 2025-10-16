x = 20
y = 22
z = 23
if x > y and x >= y:
    print('x is greater than y')
elif z == y or z <= y:
    print("z and y is equal")
elif x != y and x < y:
    print("Not working")
else:
    print('y is greater than x')


if x < z: print('Hello')

print(x) if x < z else print(z) 

print(x) if x > z else print(z) if x > y else print("ddd")

if x < y:
    pass

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

if not x < z:
   print("z is dddd")