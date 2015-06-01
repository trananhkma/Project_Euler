for a in xrange(100, 500):
    for b in xrange(100, 500):
        for c in xrange(100, 500):
            if a**2 + b**2 == c**2 and a + b + c == 1000 and a < b < c:
                print a, b, c, a*b*c
                break

#31875000            