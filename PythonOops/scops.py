x = 20

def func():
    y=23
    print(x, y)

print(x)
func()

def outerfunc():
    q = 24

    def innerfunc():
        print(q)
    
    innerfunc()

outerfunc()

ww = 34
def value():
    # print(ww) error bacause of hosting 
    ww = 22
    print(ww)

value()
print(ww)

def func2():
    global ff
    ff = 44
    print(ff)
func2()
print(ff)

rrr = 300

def func3():
    global rrr
    rrr = 34
    print(rrr)

func3()
print(rrr)


def outerfunc():
    q = 24

    def innerfunc():
        nonlocal q
        q = 55
        print(q)
    
    innerfunc()
    print(q)

outerfunc()