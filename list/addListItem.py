thislist = ["apple", "banana", "cherry"]

thislist.append(1)

print(thislist)

thislist.insert(2, '33')

print(thislist)

newList = [True, False]

thislist.extend(newList)

print(thislist)

newList.extend(thislist)

print(newList)

newList.extend('True')

print(newList)