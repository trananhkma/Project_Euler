temple = 0
for a in xrange(10,1000):
    for b in xrange(10,1000):
        c = a * b
        if c > temple and str(c) == str(c)[::-1]:
            temple = c
            print temple, a, b

#906609 913 993
