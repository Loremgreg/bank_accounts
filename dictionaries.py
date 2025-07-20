band = {"vocals": "Plant", "guitar": "Page"}

band2 = dict(vocals="Plant", guitar="Page")


print(band)
print(band2)
print(type(band))
print(len(band))

# Access items
print(band["vocals"])
print(band["guitar"])

# list all keys
for keys in band.keys():
    print(keys)

# list all values
for values in band.values():
    print(values)

# list of key/value pairs as tuples
for item in band.items():
    print(item)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})
print(band)

# Remove items
print(band.pop("bass"))
print(band)


band["drums"] = "Bonham"
print(band)

print(band.popitem())  # tuple
print(band)

for item in band.items():
    print(item)

# Delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2


