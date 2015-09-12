with open('p022_names.txt') as f:
    _input = f.readline().strip('"').split('","')
print sum([sum((ord(j)-96) for j in i.lower()) * (sorted(inter).index(i)+1) for i in _input])

# 871198282
