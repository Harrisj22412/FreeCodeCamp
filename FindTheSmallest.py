smallestNum = -1
print('Before', smallestNum)
for num in [9, 41, 12, 3, 74, 15]:
    if num < smallestNum:
        smallestNum = num
    print(smallestNum, num)
print('After', smallestNum)