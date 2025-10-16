set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

set5 = set1.union(set2)
set6 = set3 | set4
print(set5)
print(set6)

set7 = set1.union(set2, set3, set4)
set8 = set1 | set2 | set3 | set4

print(set7, set8)

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

set1.update(set2, {'22'})


print(set1)

qqq = {"apple", "banana", "cherry"}
www = {"google", "microsoft", "apple"}

eee = qqq.intersection(www)
rrr = qqq & www
print(eee, rrr)

qqq.intersection_update(www)
print(qqq)

dd = {"apple", 1,  "banana", 0, "cherry"}
ff = {False, "google", 1, "apple", 2, True}

set3 = dd.intersection(ff)

print(set3)
nn = dd.difference(ff)
print(nn) 
aa = dd - ff
print(aa)

dd.difference_update(ff)
print(dd)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

set4 = set1 ^ set2
print(set4)

set1.symmetric_difference_update(set2)

print(set1)

