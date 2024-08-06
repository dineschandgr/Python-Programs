import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")


#findall() function

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

#search() function
txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
print("The last white-space character is located in position:", x.end())

txt = "The rain in Spain"
x = re.search("ai", txt)
print("search ",x)

#split() function

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

#sub() function

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#Match object

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

txt = "The rain in Spains"
x = re.search(r"\bS\w+", txt)
print("span ",x.span())

txt = "The rain in Spain"
x = re.search(r"\br\w+", txt)
print("search ",x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print("group ",x.group())