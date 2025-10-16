import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
print(x.span())
print(x.string)
print(x.group())

import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))
