fruits = ["Apple","Orange","Mango","Banana","Apple","Kiwi"]

print(fruits[1])
print(fruits[-1])

fruits1 = fruits[: : -1]
print("reverse",fruits1)
fruits1.remove("Kiwi")
fruits1.insert(4,"Blackberry")
print("fruits",fruits1)

#ascending order
fruits1.sort()

#descending order
fruits.sort(reverse=True)
print("fruits1 sort ",fruits1)
print("fruits sort ",fruits)

#copying a list
list1 = ["apple", "banana", "cherry"]
print("list1 ",list1)
list2 = list1
print("list 2 ",list2)
count = list1.count("apple")
print("count of apple ",count)
print("count of apple ", fruits.count("Apple"))

#append
list2.append("strawberry")
print("list 2 ",list2)

list1 = [10,20,30]
print("sum ",sum(list1))

#join lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)