import functions


functions.my_function_1()
fruits = ["Apple","Orange","Mango","Banana","Apple","Kiwi"]

print(fruits[1])
print(fruits[-1])
a = "hello"
fruits1 = fruits[: : -1]

fruits1.remove("Kiwi")
fruits1.insert(4,"Kiwi")
print("reverse",fruits1)

#length of a list
print("length of fruits is ",len(fruits))

#for each loop
for ele in fruits:
    if ele == "Banana":
        continue
    print("element is ",ele)

#for loop
for i in range(0,len(fruits)):
    if i == 3:
        continue
    print(fruits[i])


vehicle = [ ["Kia","Hyundai"], "Truck", "Bus" ]
print("vehcile list",vehicle)

for ele in vehicle:
    print("element ",ele)

for i in range(0,len(vehicle)):
    if i == 0:
        car = vehicle[0]
        print("1st {} 2nd {}".format(car[0], car[1]))
    else:
        print(vehicle[i])


#sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print("sort",thislist)

#copying a list
list1 = ["apple", "banana", "cherry"]
list2 = list1
list2.append("a")
print(list1)

list1 = [10,20,30]
print("sum ",sum(list1))

list3 = list1.copy()
list3.append("b")
print(list1)

list4 = list(list1)
list4.append("c")
print(list1)

#joining lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list2[2] = 1000001

for x in list2:
  list1.append(x)

print(list1)
list1.count("apple")

#remove element in a list
list1.remove("a")
list1.pop(1)
del list1[0]
list1.clear()
del list1

