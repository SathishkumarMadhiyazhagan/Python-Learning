class firstclass:
    x = 45

a = firstclass()
print(a.x)

class newclass:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

q = newclass("sssssss", "fffffff")
print(q.firstname, q.lastname)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

class Person1:
   def __init__(self, company, address, mobile):
      self.company = company
      self.address = address
      self.mobile = mobile

   def __str__(self):
       return f"Name of company is {self.company} with addess of {self.address} {self.mobile}s"
   
p1 = Person1("XYZ", "Tamilnadu - 635205", 894984)
print(p1)

class Person2:
   def __init__(self, company, address, mobile):
      self.company = company
      self.address = address
      self.mobile = mobile
    
   def __str__(self):
      return f"Name of company is {self.company} with addess of {self.address} {self.mobile}s"
   
   def displayMethod(nn):
      print("Hello World", nn.mobile)

   def callvalue(self):
      print("Hello World")
      pass
   
    
   
p2 = Person2("XYZ", "Tamilnadu - 635205", 894984)
p2.displayMethod()

# del p2.company
print(p2.company)

# del p2
print(p2)
print(p2.callvalue())
       
