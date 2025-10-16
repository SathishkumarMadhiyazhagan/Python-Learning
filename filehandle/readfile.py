f = open("../hello.py")
print(f.read())

q = open("../range.py")
print(q.read())

with open("../tryexcept.py") as w:
    print(w.read())

# s = open("../userinput.py")
# print(s.read())

f.close()
q.close()
# w.close()

s = open("../userinput.py")
print(s.read())
s.close()

with open("../none.py") as ee:
    print(ee.read(5))
    
with open("../variable.py") as ww:
    print(ww.readline()) 
    print(ww.readline())       
    print(ww.readline())

with open("../lambda.py") as rr:
    for x in rr:
        print(x)
    
tt = open("../bool.py")

for i in tt:
    print(i)