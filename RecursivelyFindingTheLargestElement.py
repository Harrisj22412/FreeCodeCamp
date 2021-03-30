#input: a non-empty list
#returns: the largest element in this list
#1. compare the first element to largest element in the rest of the list
#values[1:] - is everything but the first element. 

def mymax(values):
    if len(values) == 1:
        return  values[0]
    else:
        max_integer = mymax(values[1:])
        if values[0] > max_integer:
            return values[0]
        else:
            return max_integer
