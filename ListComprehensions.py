#List Comprehensions 
print([111 * n for n in range(1,5)])
print([s[0] for s in ['python', 'is', 'fun']])
print([s[-1] for s in ['python', 'is', 'fun']])
print([3 * n for n in range(6) if n % 2 == 0])
print([6 + m for m in range(10) if m % 2 == 0])
print([l for l in ['Good', 'morning', 'today', 'is', 'a', 'nice', 'day'] if len(l) > 3])