a, b = 10, 3

# Arithmetic Operators
print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a // b)  # Floor Division: 3
print(a % b)   # Modulus: 1
print(a ** b)  # Exponentiation: 1000

# Assignment Operators
c = a
c += b        # c = c + b -> 13
print(c)
c -= b        # c = c - b -> 10
print(c)
c *= b        # c = c * b -> 30
print(c)
c /= b        # c = c / b -> 10.0
print(c)
c //= b       # c = c // b -> 3.0
print(c)
c %= b        # c = c % b -> 0.0
print(c)
c = a
c **= b       # c = c ** b -> 1000
print(c)

# Comparison Operators
print(a == b)   # Equal: False
print(a != b)   # Not equal: True
print(a > b)    # Greater than: True
print(a < b)    # Less than: False
print(a >= b)   # Greater or equal: True
print(a <= b)   # Less or equal: False

# Logical Operators
x, y = True, False
print(x and y)  # Logical AND: False
print(x or y)   # Logical OR: True
print(not x)    # Logical NOT: False

# Bitwise Operators
print(a & b)    # Bitwise AND: 2
print(a | b)    # Bitwise OR: 11
print(a ^ b)    # Bitwise XOR: 9
print(~a)       # Bitwise NOT: -11
print(a << 2)   # Bitwise left shift: 40
print(a >> 2)   # Bitwise right shift: 2

# Identity Operators
print(a is b)   # False
print(a is not b) # True

# Membership Operators
lst = [1, 2, 3, 10]
print(a in lst)     # True
print(b not in lst) # True

# Ternary Operator (Conditional Expression)
max_value = a if a > b else b
print(max_value)  # 10

# Chained Comparisons
print(1 < b < a)  # True

# Using operators with strings
s1, s2 = "Hello", "World"
print(s1 + " " + s2)  # Hello World
print(s1 * 3)         # HelloHelloHello
print("H" in s1)      # True
print("z" not in s2)  # True
