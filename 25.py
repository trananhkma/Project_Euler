a = 1
b = 1
count = 2
while True:
    a += b
    count += 1
    b += a
    count += 1
    if len(str(a)) == 1000 or len(str(b)) == 1000:
        print count
        break

# 4782