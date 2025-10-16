x = "eerskjfkjffklmfl"
print(len(x))

y = ['eee', 1, 22, 44, True]
print(len(y))

z = {'ee', 33, "kd"}
print(len(z))

w = {"ee": 33, "eww": 44}
print(len(w))

v = ("ee", "rr", 33)
print(len(v))

class Person:
    def __init__(self, name, age, gender, dob):
        self.name = name
        self.age = age
        self.gender = gender
        self.dob = dob
    
    def displayDetails(self):
        print(f"Details of Person {self.name}, {self.age}, {self.gender} {self.dob}")

class Job(Person):
    def __init__(self, name, age, gender, dob, company, role, designation):
        super().__init__(name, age, gender, dob)
        self.company = company
        self.role = role
        self.designation = designation
    
    def displayDetails(self):
        super()
        print(f"Details of Job {self.company}, {self.role}, {self.designation}")

        

p = Person("Sathis", 26, "Male", "01/10/1999")
p.displayDetails()

j = Job("Sathis", 26, "Male", "01/10/1999", "Candesent", "Developer", "Software Engineer")
j.displayDetails()

for x in (p, j):
    x.displayDetails()


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()