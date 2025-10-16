def decoratorFunc(func):
    def inner():
        return func().upper()
    return inner

@decoratorFunc
def newfunction():
    return "Hi I am Sathish"

@decoratorFunc
def anotherFunction():
    return "Hello World"

x = newfunction()
y = anotherFunction()
print(x)
print(y)

def decoratorWithArguments(func):
    def inner(name, age):
        if age < 18:
            return "Sorry " + name + ", you are not allowed to access this page."
        else:
            return func(name, age).upper()
    return inner

@decoratorWithArguments
def welcome(name, age):
    return "Welcome " + name + ", you are allowed to access this page."

print(welcome("Sathish", 17))
print(welcome("Sathish", 18))
print(welcome("Sathish", 20))


def argsandkwargs(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@argsandkwargs
def myfunction(nam, rr):
  return "Hello " + nam+ " " + rr

print(myfunction("John", "Doe"))

def decoratorWithArguments(n):
    def decoratorWithArguments(func):
        def inner():
            if n==1:
                return func().lower()
            else:
                return func().upper()
        return inner
    return decoratorWithArguments

@decoratorWithArguments(1)
def func():
    return 'Hello, Wellcome to python'

print(func())

def multipleDecorators(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@multipleDecorators
@addgreeting
def myfunction():
  return "Tobias"

print(myfunction())

def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)


import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)
