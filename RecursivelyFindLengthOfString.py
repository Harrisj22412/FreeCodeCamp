#Base case - When can I determine the length of the s without looking at a smaller string?
#recusrsive Substructure - How could I use the length of anything smaller than s to determine the length of s?

def mylen(s):
# returns the number of characters in s 
#input s: an arbitrary string
    if s =='':
        return 0
    else:
        length_rest_of_string =mylen(s[1:])
        return length_rest_of_string + 1

