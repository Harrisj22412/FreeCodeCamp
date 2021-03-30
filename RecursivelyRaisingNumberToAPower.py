#Base case question - When can I determine b to the power without determining a smaller power?
#recursive case question - How could I use anything smaller than b to the power to determine b to the power?

def power(b, p):
# returns b raised to the p power
#inputs: b is a number (int or float)
# p is a non- negative integer
    if p == 0: #base case
        return 1 #base case
    else:  #recursive case
        power_rest = power(b, p - 1) #recursive case
        return  b * power_rest # recursive case
