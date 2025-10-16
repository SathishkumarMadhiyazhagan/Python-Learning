x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

y = x.copy()
print(y)

a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.difference(b))
print(a - b)
print(a.intersection(b))
print(a & b)

a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))

a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)

b = frozenset({1, 2})
a = frozenset({1, 2, 3})
print(a.issuperset(b))
print(a >= b)
print(a > b)

x = a.union(b)
y = a | b
print(x,y)

z = a.symmetric_difference(b)
w = a ^ b
print(z, w)
