def hello():
    print("Hello")

hello()

def getName(firstName, lastName):
    print(f"My full name is {firstName} {lastName}")

getName("S", "M")

def arbitraryArguments(*args):
    print(args[1])

arbitraryArguments('ee', 22, True, 'ew')

def keywordArguments(child1, child2, child3):
    print(child1, child2, child3)

keywordArguments(child1='ww',child2='ee',child3='rr')

def arbitraryKeywordArguments(**args):
    print(args)

arbitraryKeywordArguments(ee='eee', dd='ddddd')

def defaultParameter(value = 'kumar'):
    print(f"hello {value}")

defaultParameter("sathis")
defaultParameter()
defaultParameter(True)

def returnValues(str):
    return str[2:4]

x = returnValues("jhdbjbdjkjc")
print(x)

def passStatment():
    pass

passStatment()

def passingListArgument(list):
    for x in list:
        print(x)

x = [22,33,4,55]
passingListArgument(x)

def positionalOnlyArguments(value, /):
    print(value)

positionalOnlyArguments(3)

def keywordOnlyArguments(*, key):
    print(key)

keywordOnlyArguments(key = 4)

def combinePositionalandKeyword(a, b, /, *, c, d):
    return a+b+c+d
a = combinePositionalandKeyword(2,3,c=44,d=55)
print(a)

def findFactorialRecursion(value):
    if value <= 1:
        return 1
    return value*findFactorialRecursion(value-1)

x = findFactorialRecursion(12)
print(x)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)


