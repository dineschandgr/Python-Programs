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


vehicle = [ ["Kia","Hyundai"], "Truck", "Bus" ]
print(vehicle)

for ele in vehicle:
    print(ele)

for i in range(0,len(vehicle)):
    if i == 0:
        car = vehicle[0]
        print( "1st {} 2nd {}".format(car[0], car[1]))
    else:
        print(vehicle[i])