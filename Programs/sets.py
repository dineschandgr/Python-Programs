from unittest import skip

set1 = {"apple","banana","mango"}
print(set1)

#unique elements
set1 = {"apple","banana","mango","apple"}
print(set1)

setfruits = {"Apple","Orange","Mango","Banana","Apple"}
print("Setfruits ",setfruits)
for i in range(0,len(setfruits)):
    skip
    #print(setfruits[i])

for item in setfruits:
    print(item)



#True=1
#False=0
set2 = {1,2,True,2,False,0,-1}
print(set2)

print(len(set2))
print(type(set2))

list1 = ["apple","mango","banana"]
set3 = set(list1)
print(set3)

print("banana" in set3)

print("strwaberry" not in set3)

#adding element to set
set3.add("blueberry")

#adding a set to set
set3.update(set1)

#adding any iterable to set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)

#remove elements - cannot access any element by index
thisset.remove("cherry")
thisset.pop()
thisset.clear()
del thisset

#joining sets

#union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set3 = set1 | set2
print(set3)

set3 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3)

#Join set and Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = [5,7,9]
a1 = x.union(y,z)
print(a1)

#intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

set3 = set1 & set2
print(set3)

#updates original set
set1.intersection_update(set2)

#difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

set3 = set1 - set2
print(set3)

#difference update
set1.difference_update(set2)

#Symmetric Differences
#keep the elements that are not present on both sides
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

set3 = set1 ^ set2
print(set3)

set1.symmetric_difference_update(set2)
print(set1)