# If we just want to search and know if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for.

found = False
print('Before', found)
for arr in [9, 41, 12, 3, 74, 15]:
    if arr == 3:
        found = True
    print(found, arr)
print('After', found)