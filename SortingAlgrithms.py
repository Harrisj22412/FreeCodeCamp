#Write a function that takes in an array of integers and sorts the integers from smallest to largest, and returns that sorted array. Please use a for loop and do not use any built in sort functions from Python. Your input is an array of integers and your output is also an array of integers.

def function(arr):
    index_len = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_len):
            if(arr[i] > arr[i + 1]):
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
























