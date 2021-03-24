import math

def square_diff(val1, val2):
    d = val1 - val2
    return d ** 2

def distance(x1,x2,y1,y2):
    distanceBetween = square_diff(x1,x2) 
    distanceBetween = distanceBetween + square_diff(y1,y2)
    newDistance = math.sqrt(distanceBetween)
    return newDistance

newDistance = distance(2,3,5,7)
print('distance between (2,3) and (5,7) is', newDistance)
