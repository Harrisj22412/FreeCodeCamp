filename = input('Enter the file name:  ')
try:
    filename = open(filename)
except:
    print('File cannot be opened:', filename)
    quit()

count = 0
for line in filename:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', filename)