thislist = ["apple", "banana", "cherry"]
thislist1 = thislist
print(thislist, thislist1)
x = thislist.copy()
print(x)

thislist[2] = '33'
print(thislist1, thislist)

z = list(thislist)
thislist[1] = '3222'
print(thislist1, thislist)
print(z)

a = thislist[:]
print(a)


