filehandle = open('ParseTextString.py')
for line in filehandle:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)