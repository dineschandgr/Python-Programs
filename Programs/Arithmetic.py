print("hello world")

a = 3
b = 2
c = a + b
print(a > b)


list = ["hello","world"]
list1 = ["hello","world"]

list2 = list
print("test in operator ", list1 in list)
print("test is operator ", list1 is list)
print("list2 = list ", list2 is list)

print("value ",not((a > b) and (c > b) and (c < a)))

count = 0
while (count == 0):
    i = int(input("Enter a value greater than 100"))
    if i > 100:
        print("success")
        break