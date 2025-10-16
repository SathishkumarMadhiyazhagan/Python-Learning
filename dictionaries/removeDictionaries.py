thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "price": 2200000
}

thisdict.pop('year')
print(thisdict)

thisdict.popitem()
print(thisdict)

thisdict.clear()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "price": 2200000
}

del thisdict['model']
print(thisdict)

del thisdict

# print(thisdict)