for x in range(1, 101):
  print(x)

i = 1
while i < 101:
  print(i)
  i += 1


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