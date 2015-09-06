with open('p022_names.txt') as f:
    inter_ = f.readline().strip('"').split('","')
print sum([sum((ord(j)-96) for j in i.lower()) * (sorted(inter).index(i)+1) for i in inter])

# 871198282
