fruits = ["Apple","Orange","Mango","Banana","Apple"]

print(fruits[1])
print(fruits[-1])

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

