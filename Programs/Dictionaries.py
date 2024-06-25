#ordered, changeable and unique keys

employeeDict = {
  "name": "Test",
  "email": "a@a.com",
  "Age": 25,
  "Age": 26
}
print(employeeDict)

#constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

print(employeeDict["name"])

print(employeeDict.get("name"))

#get all keys
print("keys ",employeeDict.keys())

#get all values
print(employeeDict.values())

#get both keys and values
print("items ",employeeDict)

# looping
# keys
for x in employeeDict:
  print(x)

for x in employeeDict.keys():
  print(x)

# values
for x in employeeDict:
  print(employeeDict[x])

for x in employeeDict.values():
  print(x)

# items
for x, y in employeeDict.items():
  print(x, y)

#check if key exists
if "email" in employeeDict:
  print("email key found")

print(len(employeeDict))


employeeDict = {
  "name": "Test",
  "email": "a@a.com",
  "Age": 25,
  "address": ["billing", "residential", "office"]
}

print(type(employeeDict))

#modification

employeeDict["name"] = "white"
employeeDict.update({"email": "C@c.com"})
print(employeeDict)

employeeDict.update({"phone": 12345})


#copy
mewdict = employeeDict.copy()
newdict1 = dict(employeeDict)

#remove
employeeDict.pop("name")
employeeDict.popitem()
del employeeDict["email"]
employeeDict.clear()
del employeeDict


#Nested

Office = {
  "employee1" : {
    "name" : "John",
    "year" : 2004
  },
  "employee2" : {
    "name" : "Steven",
    "year" : 2007
  },
  "employee3" : {
    "name" : "Hopkins",
    "year" : 2011
  }
}

employee1 = {
    "name" : "John",
    "year" : 2004
  }

employee2 = {
    "name" : "Steven",
    "year" : 2007
  }

employee3 = {
    "name" : "Hopkins",
    "year" : 2011
  }

newOffice = {
  "employee1": employee1,
  "employee2": employee2,
  "employee3": employee3
}

print("new office",newOffice["employee2"]["year"])

for x, obj in newOffice.items():
  print("1d ",x)

  for y in obj:
    print("2d", y + ':', obj[y])