for x in range(1, 101):
  if x % 5 == 0:
      continue
  print(x)

str = "welcome"
reverse = ""
for i in range(len(str) - 1,-1, -1):
    print("index ",str[i])
    reverse += str[i]
print("reverse ",reverse)

for i in str:
    print("foreach loop ",i)
else:
    print("for else")

i = 1
while i < 101:
  print("while loop ",i)
  i += 1
else:
    print("break")

while True:
    print("Enter a input between 1 to 100 ")
    int1 = int(input())
    if int1 > 1 and int1 < 101:
        print("input ", int1)
        break


l = ["geeks", "for", "geeks"]

for i in l:
    print(i)

for i in range(len(l)):
    if(l[i] == "for"):
        continue
    print(l[i])

fruits = ["apple", "orange", "kiwi"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break

list = ["apple","banana","cherry"]

for i in range(0, len(list)):
    print("list ",list[i])

for i in list:
    print(i)