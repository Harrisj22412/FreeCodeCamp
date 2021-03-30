string = 'thisisastring'
counter = 0

def countABC(word):
    counter = 0
    for letter in word:
        if letter == 'a' or letter == 'b' or letter == 'c':
            counter = counter + 1
    print(counter)

countABC('thisisastring')

