a = 1
b = 2
sum = 0
while True:
    if not a % 2:
        sum += a
    if not b % 2:
        sum += b
    a += b
    b += a
    if a > 4000000 or b > 4000000:
        break

print sum
