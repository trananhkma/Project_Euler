sum_nums = 0
count = 1
while count < 1000:
    if count % 3 == 0 or count % 5 == 0:
        sum_nums += count
    count += 1

print sum_nums

