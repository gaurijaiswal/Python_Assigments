items = list(map(int, input("Enter item numbers: ").split()))

# a) Total number of items
print("Total items:", len(items))

# b) Last item
print("Last item:", items[-1])

# c) Sorted list
print("Sorted list:", sorted(items))

# d) Check item 515
if 515 in items:
    print("Yes")
else:
    print("No")

# e) Add items and sort
items.extend([121, 321])
items.sort()
print("Updated list:", items)