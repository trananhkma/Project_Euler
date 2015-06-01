def items(x):
    count = 1
    while x > 1:
        if not x % 2:
            x /= 2
            count += 1
            if x == 1:
                return count
        else:
            x = 3*x + 1  
            count += 1

max = 0
for i in xrange(10000, 1000000):   
    if items(i) > max:
        max = items(i)
        print i, items(i)

# 837799 525
