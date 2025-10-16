value = ['hi', 'hello']
print(value)
print(len(value))
print(value[0], value[len(value)-1])

multi = ['price', 33, True, f'{34:.2f}']
print(multi)
print(type(multi))

multi[len(multi) - 1] = 'ee'
print(multi)
multi[2] = '55'
print(multi)


print(list('ee'))
a = list(('ee', '44'))
print(a)
