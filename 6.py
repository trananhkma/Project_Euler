sum_square = 0
sum_nums = 0
for i in xrange(1,101):
    sum_nums += i**2
    sum_nums += i

square = sum_nums ** 2
print square - sum_square

