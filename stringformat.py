print(f'Hello World')
print(f'Welcome {'sathish'}')
age = 23
print(f'age was {age}')
print(f'Height of {4.5:.2f}')
year = 4.3
print(f'year of experince {year:.2f}')
print(f"calculate add operation {22+33}")
print(f"calculate add operation {"ww"+"333"}")
print(f"Multiple operation of math {(year*age)+24}")
print(f"Using if else {age if age < 25 else "Age is Greater"}")
qq = "Hello World"
print(f"Hello World {"eee".upper()}")
print(f"Qwww {qq.upper()}")

def newfunc():
    return "Too"

print(f"Hel thing {newfunc()}")

def add(x):
    return x*12

print(f"Multiplecation value {add(24)}")

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

txt = "the value {}"
qq = txt.format(2)
print(qq)

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))





