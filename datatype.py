
# Demonstration of various data types in Python
int_var = 20
print(int_var, type(int_var))

float_var = 20.5
print(float_var, type(float_var))

complex_var = 1j
print(complex_var, type(complex_var))

list_var = ["apple", "banana", "cherry"]
print(list_var, type(list_var))

tuple_var = ("apple", "banana", "cherry")
print(tuple_var, type(tuple_var))

range_var = range(6)
print(range_var, type(range_var))

dict_var = {"name": "John", "age": 36}
print(dict_var, type(dict_var))

set_var = {"apple", "banana", "cherry"}
print(set_var, type(set_var))

frozenset_var = frozenset({"apple", "banana", "cherry"})
print(frozenset_var, type(frozenset_var))

bool_var = True
print(bool_var, type(bool_var))

bytes_var = b"Hello"
print(bytes_var, type(bytes_var))

bytearray_var = bytearray(5)
print(bytearray_var, type(bytearray_var))

memoryview_var = memoryview(bytes(5))
print(memoryview_var, type(memoryview_var))

none_var = None
print(none_var, type(none_var))

# Setting specific data types using constructors
int_var2 = int(10)
print(int_var2, type(int_var2))

float_var2 = float(10)
print(float_var2, type(float_var2))

complex_var2 = complex(1)
print(complex_var2, type(complex_var2))

str_var = str("Hello")
print(str_var, type(str_var))

list_var2 = list(("apple", "banana", "cherry"))
print(list_var2, type(list_var2))

tuple_var2 = tuple(("apple", "banana", "cherry"))
print(tuple_var2, type(tuple_var2))

range_var2 = range(3)
print(range_var2, type(range_var2))

dict_var2 = dict(name="Jane", age=25)
print(dict_var2, type(dict_var2))

set_var2 = set(("apple", "banana", "cherry"))
print(set_var2, type(set_var2))

frozenset_var2 = frozenset(("apple", "banana", "cherry"))
print(frozenset_var2, type(frozenset_var2))

bool_var2 = bool(1)
print(bool_var2, type(bool_var2))

bytes_var2 = bytes(5)
print(bytes_var2, type(bytes_var2))

bytearray_var2 = bytearray(5)
print(bytearray_var2, type(bytearray_var2))

memoryview_var2 = memoryview(bytes(5))
print(memoryview_var2, type(memoryview_var2))