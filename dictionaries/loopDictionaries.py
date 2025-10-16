thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "price": 2200000
}

for x in thisdict:
    print(x, thisdict[x])

# for i in range(len(thisdict)):
#     print(thisdict[i])

# j = 0
# while j < len(thisdict):
#     print(thisdict[j])
#     j+=1

for i in thisdict.keys():
    print(thisdict[i])

for i in thisdict.values():
    print(i)

for i, j in thisdict.items():
    print(i, j)

