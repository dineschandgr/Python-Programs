print("hello world")

A = 3
B = 2
C = A + B
print(A > B)

listTest = ["hello", "world"]
list1 = ["hello", "world"]

list2 = listTest
print("test in operator ", list1 in listTest)
print("test is operator ", list1 is listTest)
print("list2 = list ", list2 is listTest)

print("value ", not ((A > B) and (C > B) and (C < A)))

COUNT = 0
while COUNT == 0:
    i = int(input("Enter a value greater than 100"))
    if i > 100:
        print("success")
        break
