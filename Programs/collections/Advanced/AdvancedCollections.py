from collections import OrderedDict, defaultdict, ChainMap, namedtuple, deque, Counter

counter = Counter(['a', 'a', 'b'])
print(counter)  # Counter({'a': 2, 'b': 1})
list1 = [1, 1, 1, 2, 2, 3]
print("count of list ", Counter(list1))

counter = Counter(a=2, b=3, c=1)
print(counter)  # Counter({'b': 3, 'a': 2, 'c': 1})

counter = Counter('aabc')
print(counter)  # Counter({'a': 2, 'b': 1, 'c': 1})

words_list = ['Cat', 'Dog', 'Horse', 'Dog']
counter = Counter(words_list)
print(counter)  # Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})

# Dictionary as argument to Counter
word_count_dict = {'Dog': 2, 'Cat': 1, 'Horse': 1}
counter = Counter(word_count_dict)
print(counter)  # Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})

special_counter = Counter(name='Test', age=20)
print(special_counter)

counter = Counter({'Dog': 2, 'Cat': 1, 'Horse': 1})
countDog = counter['Dog']
print("countDog" ,countDog)

#ordered dict

od1 = OrderedDict({1:1,2:2})
od2 = OrderedDict({2:2,1:1})
d1 = dict({1:1,2:2})
d2 = dict({2:2,1:1})

print("od1 eq od2 ", od1 == od2)
print("d1 eq d2 ", d1 == d2)

print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

d.pop('a')

# Re-inserting the same
d['a'] = 1

for key, value in d.items():
    print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

od.pop('a')

# Re-inserting the same
od['a'] = 1

for key, value in od.items():
    print(key, value)

def def_value():
    return "Not Present"

d = defaultdict(def_value)

for i in range(5):
    d[i] = i

print("default dict ", d[6])

print("Dictionary with values as list:")
print(d)


#chainmap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)

# Accessing Values using key name
print(c['a'])

# Accessing values using values()
# method

print("map ", c.maps)
print("values ", list(c.values()))

# Accessing keys using keys()
# method
print("keys ", list(c.keys()))

#add new child

dict3 = {'g': 5, 'h': 6}
chain1 = c.new_child(dict3)
print(chain1)


#named tuple

Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Test', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.age)


#dequeue

de = deque([1, 2, 3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print("The deque after appending at right is : ")
print(de)

# using appendleft() to insert element at right end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print("The deque after appending at left is : ")
print(de)

de.pop()

print(de)
de.popleft()
print(de)


#UserDict

#UserList

#UserString