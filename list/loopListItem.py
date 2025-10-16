thislist = ["apple", "banana", "cherry"]

for x in thislist:
    print(x)

print(len(thislist))

print(range(len(thislist)))

for i in range(len(thislist)): {
    print(thislist[i])
}

i=0
while i<len(thislist):
    print(thislist[i])
    i += 1

[print(i) for i in thislist]