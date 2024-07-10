print("hello world")

A = 3
B = 2
C = A + B
print(A > B)


list = ["hello","world"]
list1 = ["hello","world"]

list2 = list
print("test in operator ", list1 in list)
print("test is operator ", list1 is list)
print("list2 = list ", list2 is list)

print("value ",not((A > B) and (C > B) and (C < A)))

COUNT = 0
while (COUNT == 0):
    i = int(input("Enter a value greater than 100"))
    if i > 100:
        print("success")
        break