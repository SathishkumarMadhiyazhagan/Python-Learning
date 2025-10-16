# Variable assignment and types in Python
x = 22
X = 22
# Check if x is equal to X
if(x == X):
    print('true')
else:
    print('false')

# Multiple assignments
a,b,d = 1,33,3
print(a,b,d)
# Check types of the variables
print(type(a),type(b),type(d))
# Assign the same value to multiple variables
y=q=w = 1
print(y,q,w)
# Check types of the variables
print(type(y),type(q),type(w))

# List assignment and unpacking
friends = ['ali','ahmad','sara']
print(friends)
print(type(friends))
# Unpack the list into individual variables
q,w,e = friends
print(q,w,e)
print(type(q),type(w),type(e))
# Perform arithmetic operation
print(a+b+d)

# Global variable
v = 'hello'

# Function to demonstrate access to global variable
def func():
    v='hi'
    print(v)

func()

print(v)

# Another function to modify a global variable
def myfunc1():
  global dd
  dd = "fantastic"

myfunc1()

# Use the modified global variable
print("Python is " + dd)

