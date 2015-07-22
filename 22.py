def p22():
    with open('p022_names.txt') as f:
        inter_ = f.readline().strip('"').split('","')
        return inter_

inter = p22()
total = 0
for i in inter:
    total += sum((ord(j)-96) for j in i.lower()) * (sorted(inter).index(i)+1)

print total

# 871198282