#An average just combines the counting and sum patterns and devides when the loop is done. 

count = 0
sum = 0
print('Before', count, sum)
for array in  [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = array  + sum
    print(count, sum, array)
print('After', count, sum, sum / count)