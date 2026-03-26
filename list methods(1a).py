# Creating a list
numbers = [10, 20, 30, 40]

print("Original List:", numbers)

# append()
numbers.append(50)
print("After append:", numbers)

# extend()
numbers.extend([60, 70])
print("After extend:", numbers)

# insert()
numbers.insert(2, 25)
print("After insert:", numbers)

# remove()
numbers.remove(30)
print("After remove:", numbers)

# pop()
numbers.pop()
print("After pop:", numbers)

# index()
print("Index of 40:", numbers.index(40))

# count()
print("Count of 20:", numbers.count(20))

# sort()
numbers.sort()
print("After sort:", numbers)

# reverse()
numbers.reverse()
print("After reverse:", numbers)

# copy()
new_list = numbers.copy()
print("Copied List:", new_list)

# clear()
numbers.clear()
print("After clear:", numbers)