a = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

a[1] = 'world'
print(a)

a[1:3] = ['hello']
print(a)

a[1:2] = ['hello', 'world']
print(a)

a.insert(2, 'qqqq')
print(a)