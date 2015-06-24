a = 1
b = 2
sum_nums = 0
while True:
    if not a % 2:
        sum_nums += a
    if not b % 2:
        sum_nums += b
    a += b
    b += a
    if a > 4000000 or b > 4000000:
        break

print sum_nums

