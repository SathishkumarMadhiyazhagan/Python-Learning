x = ['hi', 'hello', 'welcome']
y = iter(x)
print(next(y))
print(next(y))
print(next(y))

q = ("eee", "rrr", "www")
w = iter(q)
print(next(w))
print(next(w))
print(next(w))

a = {'nnn', 'bbb', 'hhh'}
s = iter(a)
print(next(s))
print(next(s))
print(next(s))

d = {'key':1, "value":23, 'pair':"hello"}
f = iter(d)
print(next(f))
print(next(f))
print(next(f))

g='apple'
h=iter(g)
print(next(h))
print(next(h))
print(next(h))

mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)

mystr = "banana"
for x in mystr:
  print(x)

class MyNumber:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    x = self.a
    self.a = x+1
    return x
  
y = MyNumber()
myiter = iter(y)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class NewNumber:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a +=1
      return x
    else:
      raise StopIteration
    
v = NewNumber()
m = iter(v)

for i in m:
  print(i)