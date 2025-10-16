fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

for x in fruits:
    print(x)

for x in range(len(fruits)):
    print(fruits[x])

[print(x) for x in fruits]

y=[x for x in fruits]
print(y)

z = [x for x in fruits if 'apple' is not x]
q = [x for x in fruits if 'apple' is x]

print(z,q)

z = [x for x in fruits if 'a' not in x]
q = [x for x in fruits if 'a' in x]
print(z,q)

i=0
while i < len(fruits):
  print(fruits[i])
  i = i + 1
