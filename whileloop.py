i = 0

while i<6:
    print(i)
    i+=1

a = 0

while a < 6:
    print(a)
    if a == 4:
        break
    a+=1

b = 0
while b<6:
    b+=1
    if(b == 4):
        continue
    print(b)
else:
    print("b is greater than 6")