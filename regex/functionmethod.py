import re

txt = "The rain in Spain"

x = re.findall("in", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

x = re.search("\s", txt)
print(x.start())
if x:
  print("Yes, there is a match!")
else:
  print("No match")

ww = 'Portugal is in Europe'
x = re.search("Portugal", ww)
print(x.span())

yy = "The rain in Spain 748 3839"
x = re.split("[\d]", yy)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 2)
print(x)

x = re.sub("\s", "9", txt)
print(x)

x = re.sub("\s", "9", txt, 2)
print(x)