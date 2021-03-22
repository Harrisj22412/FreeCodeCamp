largestNumber = -1
print('Before', largestNumber)
for value in [9, 41, 12, 3, 74, 15]:
    if value > largestNumber:
        largestNumber = value
    print(largestNumber, value)
print('After', largestNumber)