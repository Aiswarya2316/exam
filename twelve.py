old = [1, 2, 2, 3, 4, 4, 5]
unique = []
for item in old:
    if item not in unique:
        unique.append(item)
print(unique) 