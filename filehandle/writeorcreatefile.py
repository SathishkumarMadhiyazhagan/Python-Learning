with open("demofile.py", 'a') as dd:
    dd.write("Hello World")

with open("demofile.py", 'r') as cc:
    print(cc.readline())

with open("demofile2.py", 'w') as hw:
    hw.write("Hello Un")

with open("demofile2.py") as dr:
    print(dr.read())

dd = open("demo3.py", 'x')
