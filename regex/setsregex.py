import re

txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:
x = re.findall("[arns]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string has any characters between a and n:
x = re.findall("[a-n]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string has other characters than a, r, or n:
x = re.findall("[^arn]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

ww = "8 times before 11:45 AM"

#Check if the string has any 0, 1, 2, or 3 digits:
x = re.findall("[123]", ww)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string has any digits:
x = re.findall("[0-9]", ww)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string has any two-digit numbers, from 00 to 59:
x = re.findall("[0-5][0-9]", ww)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string has any characters from a to z lower case, and A to Z upper case:

ww = "WWkdkd dkdksk 478487 JBHJBJ++"
x = re.findall("[a-zA-Z]", ww)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Check if the string has any + characters:
x = re.findall("[+]", ww)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

