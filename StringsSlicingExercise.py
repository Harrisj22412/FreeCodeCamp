#From the string 'Welcome to Python 101: Strings', extract text and create/print a new string that says 'Welcome Ring To Tyler'
#Every first letter in a word should be capitalized(title format)
#Print the same string backwards...

msg = 'Welcome to Python 101: Strings'
msg1 = msg[18] + ' ' + msg[:8] + msg[25:29] + msg[7:11].title() + msg[13] + msg[12] + msg[2] + msg[1] + msg[25]
msg2 = msg1.title()

   


print(msg2[::-1])
#[::-1] makes the string print backwards
