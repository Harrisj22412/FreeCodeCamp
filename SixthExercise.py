smallest = None
print('Before:', smallest)
for array in [3,41,12,9,74,15]:
    if smallest is None or array < smallest:
        smallest = array
        print('Loop:', array, smallest)
print('Smallest:', smallest)