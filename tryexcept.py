try:
    print(x)
except:
    print("An exception occurred")

# print(x)

try:
    print(x)
except NameError:
    print("An exception occurred")
except:
    print("Something else went wrong")

try:
    print("Hello")
except:
    print("Error was there")
else:
    print("No Error")

try:
    print(q)
except NameError:
    print("NameError was showing")
except:
    print("Error was there")
else:
    print("No Error")

try:
    print(q)
except NameError:
    print("NameError was showing")
except:
    print("Error was there")
else:
    print("No Error")
finally:
    print("Finally Block Executed")

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

x = -1

if x < 0:
    raise Exception("Sorry no number below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")