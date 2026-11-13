import itertools

count = 0
for s in itertools.product('БОРИС', repeat=6):
    line = ''.join(s)
    if line.count('Б') == 1 and line.count('Р') == 1 and line.count('С') < 2:
        count += 1
print(count)