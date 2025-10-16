thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict['brand'] = 'bskjkskjv'
print(mydict)
print(thisdict)

dd = dict(thisdict)
print(dd)
