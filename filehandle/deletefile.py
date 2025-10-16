import os

# os.remove("demofile.py")

if os.path.exists("demo3.py"):
    os.remove("demo3.py")
else:
    print("file is not exits")

# os.rmdir("heelo")