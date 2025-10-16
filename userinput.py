import math
# print("Enter Your Value or Name")
# x = 1
# while x < 10:
#     q = input()
#     print(q
#     x+=1

# name = input()
# print(f"Hello {name}")

# x = input("Enter your age")
# txt = 'Age is {}'
# print(txt.format(x))

# name = input("Enter your name:")
# print(f"Hello {name}")
# fav1 = input("What is your favorite animal:")
# fav2 = input("What is your favorite color:")
# fav3 = input("What is your favorite number:")
# print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# ww = input("Enter year of experince")
# YY = math.floor(float(ww))
# print(f"Age of {YY}")

ee = True

while ee == True:
    x = input("Enter number")
    try:
        x = float(x)
        ee = False
    except:
        print("error")

print("Hello")