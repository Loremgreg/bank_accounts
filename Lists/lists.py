users = ["Dave", "John", "Sara"]
data = ["Dave", "42", True]

vide = []

print(users[0])
print("Dave" in vide)
print("Dave" in data)
print("Dave" in vide)
print(users[-2])
print(users.index("Sara"))
print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("Elsa")
print(len(users))
print(users)

users += ["Jason"]
print(users)

users.extend(["Robert", "Jimi"])
print(users)
print(len(users))

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)
print(len(users))

# add 2 values
users[2:2] = ["Eddie", "Alex"]
print(users)
print(len(users))

# replace 2 values
users[1:3] = ["Robert", "JJ"]
print(users)
print(len(users))

users.remove("Bob")
print(users)
print(len(users))

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

#dave a la fin car il commence par une minuscule
users[1:2] = ["dave"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
print(nums)
nums.reverse()
print(nums)
# du + grand au petit
# nums.sort(reverse=True)
# print(nums)
print(sorted(nums, reverse=True))
print(nums)

#faire une copie de la liste originale

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples

mytuple = tuple(("Dave", 42, True))
anothertuple = (1, 4, 2, 8, 2, 2)
print(mytuple)
print(anothertuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))