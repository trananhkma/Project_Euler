sum_square = 0
sum = 0
for i in xrange(1,101):
    sum_square += i**2
    sum += i

square = sum ** 2
print square - sum_square
