# Write a program which repeatedly reads number until the user enters "done". Once "done" is entered, print out the total, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

count = 0
total = 0.0
while True:
    #this converts it to a string.
    stringval = input('Enter a number:')
    if stringval == 'done':
        break 
    try:
    #this converts it to a float. 
        floatingPointValue = float(stringval)
    #print(floatingPointValue)
    
    except:
        print('Invaild input')
        continue
    #counter pattern 
    count = count + 1
    #accumulator pattern 
    total = total + floatingPointValue
#print('All Done')
#total/count = the average
print(total, count, total/ count)