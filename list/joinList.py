list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

for x in list2:
  list1.append(x)

print(list1)

list4 = ["a", "b" , "c"]
list5 = [1, 2, 3]

list4.extend(list5)
print(list4)


fruits = ["apple", "banana", "cherry", "a", "b", "c" "cherry", "cherry"]

x = fruits.count("cherry")

print(x)

x = fruits.index("cherry")
print(x)
x = fruits.index("cherry", 3, len(fruits))
print(x)
