str22 = ["orange", "mango", "kiwi", "pineapple", "banana"]

str22.sort()

print(str22)

num = [33,44,11,23,1,44,33,7,1,6]
num.sort()
print(num)
str1 = ["orange", "mango", "kiwi", "pineapple", "banana"]

str1.sort(reverse=True)
print(str1)

num1 = [33,44,11,23,1,44,33,7,1,6]
num1.sort(reverse=True)
print(num1)


str2 = ["orange", "mango", "kiwi", "pineapple", "banana"]
num2 = [33,44,11,23,1,44,33,7,1,6]

str2.reverse()
num2.reverse()
print(str2, num2)

def myfunc(n):
  return abs(n - 50)

print(myfunc(-33))

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


qq = ["banana", "Orange", "Kiwi", "cherry"]
qq.sort(key = str.lower)
print(qq)

