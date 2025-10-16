x = ["apple", "banana", "cherry", "kiwi", "mango"]

y = []

for i in x:
    if 'a' in i:
        y.append(i)

print(y)

[print(i) for i in x]

z=[i for i in x if 'apple' is not i]
print(z)

q = [i for i in x if 'apple' is i]
print(q)

w = [i for i in x if 'a' in i]
print(w)

e = [i for i in x if 'a' not in i]
print(e)

r = [i for i in x if 'apple' != i]
t = [i for i in x if 'apple' == i]
print(r, t)

u = [i for i in range(10) if i<5]
i = [i for i in range(10)]
print(u, i)

o = [i[0].upper()+i[1:] for i in x]
print(o)

p = ['hi' for i in x]
print(p)

a = [i if i!='banana' else 'orange' for i in x]
print(a)