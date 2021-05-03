friends = ['Joe', 'Jay', 'Tom']
nums = [35,85,22,43, 14]
#1. Compare first index to second index
#2. compare 35 to 22
#3.then take 22 compare store it to a temp variable
#4. continue checking to see if 35 is less the remaining integers.
#5. check to see if temp variable is less than the remaining integers in the array.

friends.sort()

print(friends)

def mysort(arr):
    for i in range(0, arr):
        for j in range(i +1, arr):
            if(arr[i] < arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr
