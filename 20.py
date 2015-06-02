fac = 1
for i in xrange(1,101):
    fac *= i

sum = 0
for i in str(fac):
    sum += int(i)

print sum