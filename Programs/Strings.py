str = "Hello World Welcome"

# accessing the character of str at 0th index
print("index 0 is ",str[0])

# accessing the character of str at 6th index
print("index 6 is ",str[6])

# accessing the character of str at 10th index
print(str[10])

print("last value ",str[-1])

print(str[-5])

#slicing
str1 = str[: 3]
print("str1 ",str1)

print(str[: 3])

str2 = str[1 : 5 : 2]
print("str 2", str2)

print(str[1 : 5 : 2])

str3 = str[-1 : -12 : -2]
print("str3 ", str3)

print(str[-1 : -12 : -2])

str5 = "HeLLo"
print("upper ",str5.upper())
print("lower ",str5.lower())
print("swapcase ",str5.swapcase())

concatStr = str3 + str5
print("concatStr ",concatStr)
a = "Hello, World!"
print("replaced string ",a.replace("l", "J"))

txt = "We are the so-called \"Vikings\" from the north."

print("escape char ",txt)

print(len(str))
str1 = ""
for i in range(len(str)-1,-1, -1):
    str1 = str1 + str[i]
    print(str[i])
print(str1)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

age = 10
print("hello ", 1,"world ", 2)
print("hello {} world {} ".format(1,2))


